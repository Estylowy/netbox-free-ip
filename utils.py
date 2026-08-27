import ipaddress
from typing import List, Dict, Any, Optional


def get_free_ranges(prefix_str: str, used_ips: List[str]) -> List[Dict[str, Any]]:
    """Zwraca WSZYSTKIE ciągłe wolne zakresy adresów w prefiksie (nie tylko
    jeden, rozciągnięty od pierwszego do ostatniego wolnego adresu — to był
    bug w poprzedniej wersji, który liczył do zakresu też adresy zajęte
    leżące pomiędzy).
    """
    try:
        network = ipaddress.ip_network(prefix_str, strict=False)
    except ValueError:
        return []

    used_set = set()
    for ip_str in used_ips:
        try:
            addr = str(ipaddress.ip_interface(ip_str).ip)
            used_set.add(ipaddress.ip_address(addr))
        except ValueError:
            try:
                used_set.add(ipaddress.ip_address(ip_str))
            except ValueError:
                continue

    all_hosts = list(network.hosts()) if network.num_addresses > 2 else list(network)
    if not all_hosts:
        return []

    ranges = []
    range_start = None
    prev_addr = None

    for addr in all_hosts:
        if addr not in used_set:
            if range_start is None:
                range_start = addr
        else:
            if range_start is not None:
                ranges.append((range_start, prev_addr))
                range_start = None
        prev_addr = addr

    # Domknij ostatni zakres, jeśli prefiks kończy się wolnymi adresami
    if range_start is not None:
        ranges.append((range_start, prev_addr))

    results = []
    for start, end in ranges:
        results.append({
            "start": str(start),
            "end": str(end),
            "count": int(end) - int(start) + 1,
            "cidr": _best_cidr(start, end),
        })

    return results


def _best_cidr(start, end) -> Optional[str]:
    """Zwraca zapis CIDR pokrywający dokładnie zakres [start, end] — jeśli
    to jeden równy blok (np. .0-.63 -> /26). Jeśli zakres wymaga kilku
    bloków CIDR do dokładnego pokrycia, zwraca ich listę (do 3 sztuk,
    rozdzieloną przecinkiem); przy większej liczbie bloków zwraca None
    (zakres nieregularny, nie ma sensu pokazywać w jednej komórce tabeli).
    """
    try:
        summarized = list(ipaddress.summarize_address_range(start, end))
    except (ValueError, TypeError):
        return None
    if not summarized:
        return None
    if len(summarized) <= 3:
        return ", ".join(str(s) for s in summarized)
    return None

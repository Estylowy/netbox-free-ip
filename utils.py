import ipaddress
from typing import List, Dict, Any

def get_free_ranges(prefix_str: str, used_ips: List[str], max_ranges: int = 50) -> List[Dict[str, Any]]:
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

    free_addresses = [addr for addr in all_hosts if addr not in used_set]
    if not free_addresses:
        return []

    # Zwracamy tylko jeden zakres: od pierwszego do ostatniego wolnego adresu
    start = free_addresses[0]
    end = free_addresses[-1]
    count = int(end) - int(start) + 1

    return [{
        'start': str(start),
        'end': str(end),
        'count': count,
        'cidr': None,
    }]


def _best_cidr(start, end, parent):
    return None

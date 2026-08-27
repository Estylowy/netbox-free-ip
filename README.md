# netbox-ip-tools

Wersja: **1.1.0**

Plugin NetBoksa łączący dwie funkcje (dawniej dwa osobne pluginy:
`netbox_free_ip` i `netbox_ip_back`):

1. **Wolne zakresy IP** — panel na stronie prefiksu pokazujący faktyczne,
   fragmentaryczne wolne zakresy adresów (tabela + wizualna siatka + eksport
   CSV + szybkie dodawanie/usuwanie adresów).
2. **Nawigacja wstecz** — panel na stronie adresu IP z linkami do wszystkich
   prefiksów nadrzędnych zawierających ten adres.

## Naprawiony błąd (względem oryginalnego `netbox_free_ip`)

Poprzednia wersja liczenia wolnych zakresów (`get_free_ranges`) zwracała
zawsze **jeden** zakres — od pierwszego do ostatniego wolnego adresu w całym
prefiksie, **licząc też adresy zajęte leżące pomiędzy nimi**. Dla prefiksu
z adresami zajętymi gdziekolwiek poza samym początkiem/końcem dawało to
całkowicie błędny wynik (np. `/24` z zajętymi `.10`–`.240` pokazywał jeden
"wolny zakres" `.1`–`.254` z licznikiem 254, zamiast dwóch prawdziwych
fragmentów: `.1`–`.9` i `.241`–`.254`, razem 23 adresy).

Nowa wersja poprawnie identyfikuje **wszystkie** ciągłe wolne fragmenty
i dodatkowo liczy realny zapis CIDR tam, gdzie fragment jest wyrównany do
granicy bloku (np. dokładnie `/26`).

## Wymagania

- NetBox 4.3.1+
- Python 3.9+

## Instalacja

Patrz `INSTALL.md`.

## Konfiguracja (`configuration.py`)

```python
PLUGINS = [
    "netbox_ip_tools",
]

PLUGINS_CONFIG = {
    "netbox_ip_tools": {
        "max_free_ranges": 50,  # ile zakresów pokazać w tabeli na raz
    }
}
```

# Instrukcja wgrania netbox-ip-tools (scalonego: Wolne zakresy IP + Powrót do prefiksu)

## 0. Odinstaluj STARE wersje (ważne)

Jeśli masz zainstalowane `netbox_free_ip` i/lub `netbox_ip_back` osobno —
odinstaluj je najpierw, żeby uniknąć dwóch rejestracji tych samych URL-i
i rozszerzeń szablonów:

```bash
source /opt/netbox-4.5.4/venv/bin/activate
pip uninstall -y netbox-free-ip netbox_free_ip netbox-ip-back netbox_ip_back
```

## 1. Rozpakuj i zainstaluj

```bash
tar -xzf netbox_ip_tools_v1.1.0.gz -C ~/netbox_ip_tools_src
cd ~/netbox_ip_tools_src
pip install . --force-reinstall --no-deps
```

## 2. Podmień konfigurację

W `configuration.py`:

```python
PLUGINS = [
    # ... reszta Twoich pluginów ...
    "netbox_ip_tools",
    # USUŃ wpisy "netbox_free_ip" i "netbox_ip_back", jeśli tam były
]

PLUGINS_CONFIG = {
    # ... reszta ...
    "netbox_ip_tools": {
        "max_free_ranges": 50,
    },
    # USUŃ ewentualne stare bloki "netbox_free_ip" / "netbox_ip_back"
}
```

## 3. Migracje i restart

Plugin nie ma własnych modeli/migracji.

```bash
cd /opt/netbox-4.5.4/netbox
python3 manage.py collectstatic --no-input
sudo systemctl restart netbox netbox-rq
```

## 4. Weryfikacja

- Wejdź na stronę dowolnego **prefiksu** (`IPAM → Prefixes → <prefiks>`) —
  po prawej powinien być panel "Wolne zakresy IP" z tabelą i siatką.
- Wejdź na stronę dowolnego **adresu IP** — powinien być panel "Nawigacja —
  prefiksy nadrzędne".
- Sprawdź na prefiksie, gdzie zajęte adresy są **w środku** zakresu (nie na
  samym początku/końcu) — tabela powinna teraz pokazywać **kilka** wolnych
  zakresów, a nie jeden obejmujący też zajęte adresy.

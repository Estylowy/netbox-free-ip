# netbox_free_ip

NetBox 4.x plugin that brings PHP IPAM-inspired free IP range visualization to prefix detail pages.

Works on: **IPAM → Prefixes → prefix detail**

## Features

- Free IP ranges table: first address, last address, count
- Visual prefix grid — green = free, red = used
- Click a free address → modal to add a new IP
- Click a used address → modal to remove it
- Filter by status: Active, Reserved, Deprecated
- CSV export and clipboard copy
- Collapsible panel

## Installation

### 1. Upload to your server and install

```bash
cd /opt/plugins
tar xzf netbox_free_ip.tar.gz
sudo /opt/netbox/venv/bin/pip install /opt/plugins/netbox_free_ip/
```

### 2. Add to configuration.py

```python
PLUGINS = [
    "netbox_free_ip",
]

PLUGINS_CONFIG = {
    "netbox_free_ip": {
        "max_free_ranges": 50,
    }
}
```

### 3. Migrate and restart

```bash
sudo /opt/netbox/venv/bin/python /opt/netbox/netbox/manage.py migrate
sudo /opt/netbox/venv/bin/python /opt/netbox/netbox/manage.py collectstatic --no-input
sudo systemctl restart netbox netbox-rq
```

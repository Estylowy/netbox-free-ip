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

### 1. Download and install

Clone or download this repository. The folder structure must be preserved exactly as follows — pip requires it to install correctly:

```
netbox_free_ip/
├── setup.py
├── MANIFEST.in
└── netbox_free_ip/
    ├── __init__.py
    ├── views.py
    ├── urls.py
    ├── utils.py
    ├── tables.py
    ├── template_content.py
    ├── templates/
    └── templatetags/
```

If you're uploading manually (e.g. via GitHub download), make sure to recreate this folder structure on your server before installing.

```bash
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

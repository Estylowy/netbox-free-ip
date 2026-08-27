from netbox.plugins import PluginTemplateExtension


class PrefixFreeIPExtension(PluginTemplateExtension):
    model = 'ipam.prefix'

    def right_page(self):
        prefix = self.context.get('object')
        if prefix is None:
            return ''
        from ipam.models import Prefix
        if not isinstance(prefix, Prefix):
            return ''
        return self.render(
            'netbox_ip_tools/free_ip_panel.html',
            extra_context={'prefix': prefix}
        )


class IPAddressBackExtension(PluginTemplateExtension):
    model = 'ipam.ipaddress'

    def right_page(self):
        ip = self.context.get('object')
        if ip is None:
            return ''
        from ipam.models import IPAddress
        if not isinstance(ip, IPAddress):
            return ''
        return self.render(
            'netbox_ip_tools/back_button.html',
            extra_context={'ip': ip}
        )


template_extensions = [PrefixFreeIPExtension, IPAddressBackExtension]

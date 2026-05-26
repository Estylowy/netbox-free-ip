from netbox.plugins import PluginTemplateExtension


class PrefixFreeIPExtension(PluginTemplateExtension):
    model = 'ipam.prefix'

    def right_page(self):
        prefix = self.context.get('object')
        if prefix is None:
            return ''
        # Dodatkowe sprawdzenie że to na pewno Prefix
        from ipam.models import Prefix
        if not isinstance(prefix, Prefix):
            return ''
        return self.render(
            'netbox_free_ip/free_ip_panel.html',
            extra_context={'prefix': prefix}
        )


template_extensions = [PrefixFreeIPExtension]

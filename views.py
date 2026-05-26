from django.http import JsonResponse
from django.views import View
from django.shortcuts import get_object_or_404
from django.conf import settings
from ipam.models import Prefix, IPAddress
from .utils import get_free_ranges


class FreeIPRangesView(View):
    """
    GET /plugins/free-ip/prefix/<id>/free-ranges/
    """
    def get(self, request, prefix_id):
        prefix = get_object_or_404(Prefix, pk=prefix_id)
        cfg = settings.PLUGINS_CONFIG.get('netbox_free_ip', {})
        max_ranges = cfg.get('max_free_ranges', 50)

        used_ips = list(
            IPAddress.objects.filter(
                address__net_contained_or_equal=str(prefix.prefix)
            ).values_list('address', flat=True)
        )
        used_ip_strings = [str(ip).split('/')[0] for ip in used_ips]

        free = get_free_ranges(
            prefix_str=str(prefix.prefix),
            used_ips=used_ip_strings,
            max_ranges=max_ranges,
        )

        return JsonResponse({
            'prefix': str(prefix.prefix),
            'prefix_id': prefix.pk,
            'total_free_ranges': len(free),
            'results': free,
        })

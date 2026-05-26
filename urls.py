from django.urls import path
from . import views

urlpatterns = [
    path(
        'prefix/<int:prefix_id>/free-ranges/',
        views.FreeIPRangesView.as_view(),
        name='free_ip_ranges',
    ),
]

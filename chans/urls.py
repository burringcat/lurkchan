from django.urls import path, include
from django.conf import settings

from .views import *
chan_urls = [
    path('', boards),
    path('boards/', boards),
    path('<str:board>/', category, name='chan-board'),
    path('<str:board>/<int:page>/', category),
    path('<str:board>/thread/<str:thread>/', thread),
]

urlpatterns = [
    path('<str:chan_name>/', include(chan_urls))
]
if settings.LURKCHAN_REVERSE_PROXY_SUB_URL:
    urlpatterns = [
        path(settings.LURKCHAN_REVERSE_PROXY_SUB_URL, include(urlpatterns))
    ]
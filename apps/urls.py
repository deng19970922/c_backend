from django.urls import path, include

urlpatterns = [
    path('audience/', include('apps.audience.urls')),
    path('campaign/', include('apps.campaign.urls')),
    path('channel/', include('apps.channel.urls')),
    path('brand/', include('apps.brand.urls')),
    path('users/', include('apps.users.urls')),
]

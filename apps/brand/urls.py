from django.urls import path, include
from rest_framework import routers

from apps.brand import views
from apps.brand.serializers import BrandSerializer

router = routers.DefaultRouter()
router.register('brands', BrandSerializer, basename='brands')
urlpatterns = [
    path('index/', views.brand_info),
    path('', include(router.urls))
]
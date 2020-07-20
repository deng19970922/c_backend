from django.urls import path, include
from rest_framework import routers

from apps.brand import views
from apps.brand.views import BrandModelViewSet, BrandAPIView

router = routers.DefaultRouter()
router.register('brands', BrandModelViewSet, basename='brands')
urlpatterns = [
    path('index/', views.brand_info),
    path('', include(router.urls)),
    path('brand_data/', BrandAPIView.as_view()),
    path('list/', views.brand_list),
]
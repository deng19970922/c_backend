from django.urls import path

from apps.campaign import views

urlpatterns = [
    path('index/', views.index)
]
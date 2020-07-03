from django.urls import path

from apps.brand import views

urlpatterns = [
    path('index/', views.index)
]
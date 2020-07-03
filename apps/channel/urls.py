from django.urls import path

from apps.channel import views

urlpatterns = [
    path('index/', views.index)
]
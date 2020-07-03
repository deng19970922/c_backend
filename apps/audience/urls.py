from django.urls import path

from apps.audience import views

urlpatterns = [
    path('index/', views.index)
]
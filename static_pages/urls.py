from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('shop/', views.shop, name='shop'),
    path('about/', views.about, name='about'),
    path('service/', views.services, name='service'),
    path('contact/', views.contact, name='contact'),
    path('help/', views.help, name='help'),
] 
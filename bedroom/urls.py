from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='bedroom'),
    path('<int:listing_id>', views.list, name='list'),
] 
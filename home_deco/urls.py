from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home_deco'),
    path('<int:listing_id>', views.deco_list, name='deco_list'),
] 
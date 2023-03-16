from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='carbinets'),
    path('<int:listing_id>', views.carb_listing, name='carb_listing'),
] 
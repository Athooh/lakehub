from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='dining_rm'),
    path('<int:listing_id>', views.dining_listing, name='dr_listing'),
] 
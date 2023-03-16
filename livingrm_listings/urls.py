from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='living_rm'),
    path('<int:listing_id>', views.listing, name='listing'),
] 
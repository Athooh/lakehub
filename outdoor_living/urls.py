from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='outdoor'),
    path('<int:listing_id>', views.outdoor_list, name='outdoor_listing'),
] 
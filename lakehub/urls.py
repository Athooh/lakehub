from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', include('static_pages.urls')),
    path('livingrm_listings/', include('livingrm_listings.urls')),
    path('bedroom/', include('bedroom.urls')),
    path('dining_listings/', include('dining_listings.urls')),
    path('carbinets/', include('carbinets.urls')),
    path('home_deco/', include('home_deco.urls')),
    path('outdoor_living/', include('outdoor_living.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

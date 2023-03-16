from django.contrib import admin

# Register your models here.
from .models import HomeDecoListing

class HomeDecoListingAdmin(admin.ModelAdmin):
    list_display= ('listing_id', 'title','category','is_published', 'price_new', 'price_old', 'list_date')
    list_display_links = ('listing_id', 'title')
    list_filter= ('category', 'price_new')
    list_editable = ('is_published',)
    search_fields = ('title', 'description', 'made_in_location','price_new','list_date')
    list_per_page = 25
    
admin.site.register(HomeDecoListing, HomeDecoListingAdmin)
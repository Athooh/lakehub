from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import OutdoorListing


# Create your views here.
def index(request):
    outdoor_listings = OutdoorListing.objects.all()
    
    paginator = Paginator(outdoor_listings, 6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    
    context = {
            'outdoor_listings': paged_listings
     }
    
    return render(request, 'outdoor_living/outdoor.html', context)

def outdoor_list(request, listing_id):
    outdoor_listing = get_object_or_404(OutdoorListing, pk=listing_id)
    
    context = {
        'outdoor_listing': outdoor_listing
        }
    return render(request, 'outdoor_living/outdoor_listing.html', context) 
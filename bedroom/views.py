from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import BedroomListing


# Create your views here.
def index(request):
    br_listings = BedroomListing.objects.all()
    
    paginator = Paginator(br_listings, 6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    
    context = {
           'br_listings': paged_listings
    
    }
    return render(request, 'bedroom_listings/bed_rm.html', context)

def list(request, listing_id):
    br_listing = get_object_or_404(BedroomListing, pk=listing_id)
    
    context = {
        'br_listing': br_listing
        }
    return render(request, 'bedroom_listings/br_listing.html', context) 
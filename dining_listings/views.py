from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import DiningListing


# Create your views here.
def index(request):
    dining_listings = DiningListing.objects.all()
    
    paginator = Paginator(dining_listings, 6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    
    context = {
        'dining_listings': paged_listings
    }
    return render(request, 'diningrm_listings/dining_rm.html', context)

def dining_listing(request, listing_id):
    dr_listing = get_object_or_404(DiningListing, pk=listing_id)
    
    context = {
        'dr_listing': dr_listing
        }
    return render(request, 'diningrm_listings/dr_listing.html', context) 
from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import Listing


# Create your views here.
def index(request):
    livingrm_listings = Listing.objects.all()
    
    paginator = Paginator(livingrm_listings, 6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    
    context = {
        'livingrm_listings': paged_listings
    }
    return render(request, 'livingrm_listings/living_rm.html', context)

def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)
    
    context = {
        'listing': listing
        }
    return render(request, 'livingrm_listings/listing.html', context) 
from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import CarbinetsListing


# Create your views here.
def index(request):
    carbinets_listings = CarbinetsListing.objects.all()
    
    #paginator = Paginator(carbinets_listings, 6)
    #page = request.GET.get('page')
    #paged_listings = paginator.get_page(page)
    
    #context = {
    #    'carbinets_listings': paged_listings
    #}
    context = {
        'carbinets_listings': carbinets_listings
    }
    return render(request, 'carbinets/carbinets.html', context)

def carb_listing(request, listing_id):
    carb_listing = get_object_or_404(CarbinetsListing, pk=listing_id)
    
    context = {
        'carb_listing': carb_listing
        }
    return render(request, 'carbinets/carb_listing.html', context) 
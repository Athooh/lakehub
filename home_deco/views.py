from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import HomeDecoListing


# Create your views here.
def index(request):
    home_deco = HomeDecoListing.objects.all()
    
    paginator = Paginator(home_deco, 6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    
    context = {
            'home_deco': paged_listings
     }
    
    return render(request, 'home_deco/home_deco.html', context)

def deco_list(request, listing_id):
    deco_listing = get_object_or_404(HomeDecoListing, pk=listing_id)
    
    context = {
        'deco_listing': deco_listing
        }
    return render(request, 'home_deco/deco_listing.html', context) 
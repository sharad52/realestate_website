from django.shortcuts import render,get_object_or_404
from django.core.paginator import Paginator
from .models import Listings


# Create your views here.
def index(request):
	listing = Listings.objects.order_by('-list_date').filter(is_published=True)
	paginator = Paginator(listing,6)
	page = request.GET.get('page')
	paged_listings = paginator.get_page(page)

	context = { 'listing': paged_listings }
	return render(request,'listings/listings.html',context)

def listing(request,list_id):

	list_fetch = get_object_or_404(Listings,pk=list_id)

	context={
		'list':list_fetch
	}
	return render(request,'listings/listing.html',context)

def search(request):

	return render(request,'listings/search.html')
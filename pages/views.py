from django.shortcuts import render
from listings.models import Listings 
from realtors.models import Realtor
from listings.choices import price_choices,state_choices,bedroom_choices

# Create your views here.
def index(request):

	listing = Listings.objects.order_by('-list_date').filter(is_published=True)[:3]

	context = {
		'listings': listing,
		'state_choices':state_choices,
		'bedroom_choices':bedroom_choices,
		'price_choices':price_choices
	}

	return render(request,'pages/index.html',context )

def about(request):
	#Get all Realtor 
	realtors = Realtor.objects.order_by('-hire_date')

	#Get MVP
	mvp_realtors = Realtor.objects.all().filter(is_mvp=True)

	context = {
		'realtors':realtors,
		'mvp_realtors':mvp_realtors,
	}


	return render(request,'pages/about.html',context)


def search(request):
	

	return render(request,'pages/search.html')
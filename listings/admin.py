from django.contrib import admin
from .models import Listings

# Register your models here.
@admin.register(Listings)
class ListingsAdmin(admin.ModelAdmin):
	list_display = ('title','id','is_published','price','realtor',)
	list_display_link = ('id','title',)
	list_filter = ('realtor',)
	list_editable = ('is_published',)
	search_fields = ('title','address','description','city','state',)
	list_per_page = 25
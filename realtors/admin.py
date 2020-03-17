from django.contrib import admin
from .models import Realtor

# Register your models here.
@admin.register(Realtor)
class RealtorAdmin(admin.ModelAdmin):
	list_display = ('name','email',)
	search_fields = ('name','email','phone')
	list_display_link = ('name','email',)
	list_per_page = 15
	list_filter = ('name','is_mvp',)

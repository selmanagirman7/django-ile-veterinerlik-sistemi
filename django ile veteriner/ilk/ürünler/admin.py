from django.contrib import admin
from .models import ürün

class ürünkontrol(admin.ModelAdmin):
    list_display=('id', 'name', 'created_date')
    search_fields=('name', 'description')
    list_per_page=20
# Register your models here.
admin.site.register(ürün , ürünkontrol)
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import Http404
from .models import ürün

# Create your views here.

def index(request):
    movies = ürün.objects.all()

    context = {
        'ürünler': ürünler
    }
    return render(request, 'ürünler/list.html', context)

def detail(request, ürün_id):
    ürün = get_object_or_404(ürün, pk = ürün_id)
    context = {
        'ürün': ürün
    }
    return render(request, 'ürünler/detail.html', context)

def search(request):
    return render(request, 'ürünler/search.html')

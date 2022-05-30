from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='ürünler'),
    path('<int:ürün_id>', views.detail, name='detail'),
    path('search', views.search, name='search'),
    
    
]

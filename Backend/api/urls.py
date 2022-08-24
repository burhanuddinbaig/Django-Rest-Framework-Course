from django.urls import path, include

from . import  views

urlpatterns = [
    path('', views.api_home),           #localhost 8000
    path('api/products/', include('products.urls')),
]
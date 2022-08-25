from rest_framework import generics

from .models import Product
from .serializers import ProductSerializer

# Generic API Views

# Product Create View

class ProductCreateAPIView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

product_create_view = ProductCreateAPIView.as_view()

# Product Detail View

class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

product_detail_view = ProductDetailAPIView.as_view()
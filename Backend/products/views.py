from rest_framework import generics

from .models import Product
from .serializers import ProductSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

# Generic API Views

# Product Create View

class ProductCreateAPIView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        print(serializer.validated_data)
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('context') or None
        if content is None:
            content = title
        serializer.save(content = content)

product_create_view = ProductCreateAPIView.as_view()

class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('context') or None
        if content is None:
            content = title
        serializer.save(content = content)

product_list_create_view = ProductListCreateAPIView.as_view()

# Product Detail View

class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

product_detail_view = ProductDetailAPIView.as_view()

class ProductListAPIView(generics.ListAPIView):
    '''
    Not gonna use this method
    '''
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

product_list_view = ProductListAPIView.as_view()
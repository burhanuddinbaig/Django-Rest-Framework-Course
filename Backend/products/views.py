from rest_framework import generics, mixins

from .models import Product
from .serializers import ProductSerializer
from .mixins import StaffEditorPermissionMixin

from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

# Generic API Views

# Product Create View

class ProductCreateAPIView(
    StaffEditorPermissionMixin,
    generics.CreateAPIView):
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

class ProductListCreateAPIView(
    StaffEditorPermissionMixin,
    generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('context') or None
        if content is None:
            content = title
        serializer.save(content = content)


product_list_create_view = ProductListCreateAPIView.as_view()

# product mixin view

class ProductMixinView( mixins.CreateModelMixin, mixins.ListModelMixin,
                        mixins.RetrieveModelMixin, 
                        generics.GenericAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def get(self, request, *args, **kwargs):
        print(args, kwargs)
        pk = kwargs.get("pk")
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
        
    def perform_create(self, serializer):
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('context') or None
        if content is None:
            content = "this is a single view doing cool stuf"
        serializer.save(content = content)

product_mixin_view = ProductMixinView.as_view()

# Product update View

class ProductUpdateAPIView(
    StaffEditorPermissionMixin,
    generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title

product_update_view = ProductUpdateAPIView.as_view()

# Product delete View

class ProductDestroyAPIView(
    StaffEditorPermissionMixin,
    generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title

product_destroy_view = ProductDestroyAPIView.as_view()

# Product Detail View

class ProductDetailAPIView(
    StaffEditorPermissionMixin,
    generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

product_detail_view = ProductDetailAPIView.as_view()

def product_alt_view(request, pk = None, *args, **kwargs):
    method = request.method

    if method == "GET":
        if pk is not None:
            # detail view
            obj = get_object_or_404(Product, pk = pk)
            data = ProductSerializer(obj, many=False).data

            return Response(data)

        # list view
        queryset = Product.objects.all()
        data = ProductSerializer(queryset, many=True).data        
        return Response(data)

    if method == "POST":
        # create an item
        serializer = ProductSerializer(data=request.data)
        if(serializer.is_valid(raise_exception=True)):
            title = serializer.validated_data.get('title')
            content = serializer.validated_data.get('context') or None
            if content is None:
                content = title
            serializer.save(content = content)
            return Response(serializer.data)
        return Response({"invalid":"not good data"}, status = 400)
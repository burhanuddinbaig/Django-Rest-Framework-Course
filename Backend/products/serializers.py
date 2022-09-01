from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(read_only=True)
    url_edit = serializers.SerializerMethodField(read_only=True)
    url = serializers.HyperlinkedIdentityField(view_name='product-detail')
    class Meta:
        model = Product
        fields = [
            'url_edit',
            'url',
            'pk',
            'title',
            'content',
            'price',
            'sale_price',
            'my_discount',
        ]

    def get_url(self, obj):
        # return f"/api/products/{obj.pk}/"  #to get url
        request = self.context.get('request')
        if request is None:
            return None
        return reverse("product-detail", kwargs = {'pk': obj.pk}, request = request)

    def get_url_edit(self, obj):
        request = self.context.get('request')
        if request is None:
            return None
        return reverse("product-detail", kwargs = {'pk': obj.pk}, request = request)

    def get_my_discount(self, obj):
        if not hasattr(obj, "id"):
            return None
        elif not isinstance(obj, Product):
            return None
        return obj.get_discount()
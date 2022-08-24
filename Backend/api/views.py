# from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from products.models import Product
from products.serializers import ProductSerializer
from django.forms.models import model_to_dict
from rest_framework.decorators import api_view
from rest_framework.response import Response
import json

@api_view(["POST"])
def api_home(request, *agrs, **kwargs):
    """
    DRF API View
    """
    serializer = ProductSerializer(data=request.data)
    if(serializer.is_valid(raise_exception=True)):
        # instance = serializer.save()
        # print(instance)
        print(serializer.data)
        return Response(serializer.data)
    return Response({"invalid":"not good data"}, status = 400)

# @api_view(["GET"])
# def api_home(request, *agrs, **kwargs):
#     """
#     DRF API View
#     """
    # data = request.data
    # instance = Product.objects.all().order_by("?").first()

    # data = {}
    # if instance:
    #     # data = model_to_dict(instance, fields = ['id', 'title', 'price', 'sale_price'])
    #     data = ProductSerializer(instance).data



#------ for get data ------------
    #data = request.data
    # instance = Product.objects.all().order_by("?").first()

    # data = {}
    # if instance:
    #     # data = model_to_dict(instance, fields = ['id', 'title', 'price', 'sale_price'])
    #     data = ProductSerializer(instance).data








    # return HttpResponse(data, headers = {"content-type":"application/json"})          # to use Http Response

    # -----working with echo data -----------
    # # print(request.GET)
    # # print(request.POST)
    # body = request.body

    # data = {}

    # try:
    #     data = json.loads(body)
    # except:
    #     print("Error")
    # data['headers'] = request.headers
    # data['content_type'] = request.content_type
    # print(data)
    # return JsonResponse({"message":"Hi there, this is your Django API Response"})
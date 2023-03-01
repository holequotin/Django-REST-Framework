from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from api.models import Product
from django.forms.models import model_to_dict
# Create your views here.

def api_home(request):
    instance = Product.objects.get(id = 1)
    data = {}
    if instance:
        # data = {
        #     'id' : instance.id,
        #     'title' : instance.title,
        #     'descriptions' : instance.descriptions,
        #     'price' : instance.price,
        # }
        data = model_to_dict(instance,fields=['title','price'])
    return JsonResponse(data)
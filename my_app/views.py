from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, JsonResponse
from .models import Person, Products
import json

# Create your views here.
def all_users(request: HttpRequest):
    users = Person.objects.all()
    response = {'users': []}
    for u in users:
        user              = dict()
        user['firstname'] = u.first
        user['lastname']  = u.last
        print(user, type(user))
        response['users'].append(user)
    
    return JsonResponse(response)


def all_products(request: HttpRequest):
    products = Products.objects.all()
    response = {'products': []}
    for p in products:
        product            = dict()
        product['name']    =  p.name
        product['company'] =  p.company
        product['color']   =  p.color
        product['ram']     =  p.ram
        product['memory']  =  p.memory
        product['price']   =  p.price
        product['img_url'] =  p.img_url

    return JsonResponse(response)


def add_product(request: HttpRequest):
    if request.method == 'POST':
        data = request.POST
        product = Products()
        product.name    = data['name']
        product.company = data['company']
        product.color   = data['color']
        product.ram     = data['ram']
        product.memory   = data['memory']
        product.price   = data['price']
        product.img_url = data['img_url']

        product.save()
        return JsonResponse({'response': 200})
    else:
        return HttpResponse("not post")

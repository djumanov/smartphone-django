from django.shortcuts import render
from django.http import HttpRequest, JsonResponse, HttpResponse
from .models import Product

# Create your views here.
def get_products(request: HttpRequest) -> JsonResponse:
    if request.method == 'GET':
        products  = Product.objects.all()
        all_products = list()
        for product in products:
            all_products.append({
                'id':         product.id,
                'name':       product.name,
                'company':    product.company,
                'color':      product.color,
                'RAM':        product.RAM,
                'memory':     product.memory,
                'price':      product.price,
                'created_at': product.created_at,
                'updated_at': product.updated_at,
                'img_url':    product.img_url,
            })

        return JsonResponse({'products': all_products})

    return HttpResponse('Bad Request!')


def get_product(request: HttpRequest, id: int) -> JsonResponse:
    if request.method == 'GET':
        product = Product.objects.get(id=id)
        #Check if the product exists using the id    
        product_json = {
                'id':         product.id,
                'name':       product.name,
                'company':    product.company,
                'color':      product.color,
                'RAM':        product.RAM,
                'memory':     product.memory,
                'price':      product.price,
                'created_at': product.created_at,
                'updated_at': product.updated_at,
                'img_url':    product.img_url,
            }

        return JsonResponse({'product': product_json})


def add_product(request: HttpRequest) -> JsonResponse:
    if request.method == 'POST':
        data = request.POST
        new_product = Product()
        new_product.name    = data['name']
        new_product.company = data['company']
        new_product.color   = data['color']
        new_product.RAM     = data['RAM']
        new_product.memory  = data['memory']
        new_product.price   = data['price']
        new_product.img_url = data['img_url']
        new_product.save()

        product_json = {
                'id':         new_product.id,
                'name':       new_product.name,
                'company':    new_product.company,
                'color':      new_product.color,
                'RAM':        new_product.RAM,
                'memory':     new_product.memory,
                'price':      new_product.price,
                'created_at': new_product.created_at,
                'updated_at': new_product.updated_at,
                'img_url':    new_product.img_url,
            }
        return JsonResponse({'new_product': product_json})
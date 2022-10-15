from django.shortcuts import render
from django.http import HttpRequest, JsonResponse, HttpResponse
from .models import Product

# Create your views here.
def get_products(request: HttpRequest) -> list[dict]:
    if request.method == 'GET':
        products  = Product.objects.all()
        all_products = list()
        for product in products:
            all_products.append({
                'id': product.id,
                'name': product.name,
                'company': product.company,
                'color': product.color,
                'RAM': product.RAM,
                'memory': product.memory,
                'price': product.price,
                'created_at': product.created_at,
                'updated_at': product.updated_at,
                'img_url': product.img_url,
            })

        return JsonResponse({'products': all_products})

    return HttpResponse('Bad Request!')


def get_product(request: HttpRequest, id: int) -> dict:
    if request.method == 'GET':
        product = Product.objects.get(id=id)
        #Check if the product exists using the id    
        product_json = {
                'id': product.id,
                'name': product.name,
                'company': product.company,
                'color': product.color,
                'RAM': product.RAM,
                'memory': product.memory,
                'price': product.price,
                'created_at': product.created_at,
                'updated_at': product.updated_at,
                'img_url': product.img_url,
            }

        return JsonResponse({'product': product_json})

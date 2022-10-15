# SmartPhone

## List of Brands
- Apple
- Samsung
- Huawei
- Xiaomi
- Oppo
- Vivo
- Nokia

## Structure of Project
### 1. Design of The Project Database
### 2. Design of The Project Interface
### 3. Design of The Project Test
### 4. Design of The Project Report
### 5. Design of The Project Presentation

## List of Tasks

### 1. Design of The Project Database
- [ ] Create The Database
- [ ] Create The Table
- [ ] Create The Relations
- [ ] Create The Views

### 2. Design of The Project Interface
- [ ] Create The Interface
- [ ] Create The Forms
- [ ] Creare The Reports

### 3. Design pf API endpoints
- [ ] Create The API endoints
- [ ] Create The API Documentation

### 4. List of API endpoints
- [ ] GET `/api/products` - get all brands.
- [ ] GET `/api/product/<int:id>` - get a brand.
- [ ] POST `/api/add_product` - add a brand.
- [ ] POST `/api/update_product/<int:id>` - update product.
- [ ] POST `/api/delete_product/<int:id>` - delete product.

## Checklist of Tasks
### 1. Create The Virtual Enviroment
```bash
python -m venv venv
```

### 2. Install The Packages
```bash
pip install -r requirements.txt
```

### 3. Create The Project
```bash
django-admin startproject config .
```

### 4. Create APP of The Project
```bash
python manage.py startapp api
```

### 5. Create The Database of The Project
```bash
python manage.py migrate
```

### 6. Create The SuperUser
```bash
python manage.py createsuperuser
```

### 7. Create The Table of SmartPhone Schema
## Database Schema
| Field | Type | Null | Key | Default | Extra |
| --- | --- | --- | --- | --- | --- |
| id | int(11) | NO | PRI | NULL | auto_increment |
| name | varchar(255) | NO | | NULL | |
| company | varchar(255) | NO | | NULL | |
| color | varchar(255) | NO | | NULL | |
| RAM | int(11) | NO | | NULL | |
| memory | int(11) | NO | | NULL | |
| price | int(11) | NO | | NULL | |
| created_at | datetime | NO | | NULL | |
| updated_at | datetime | NO | | NULL | |
| img_url | varchar(255) | NO | | NULL | |

`api/models.py`
```python
from django.db import models
class Product(models.Model):
    name = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    color = models.CharField(max_length=255)
    RAM = models.IntegerField()
    memory = models.IntegerField()
    price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    img_url = models.CharField(max_length=255)
    def __str__(self):
        return self.name
```

### 8. Regisrtate Models
`api/admin.py`
```python
from .models import Product

tables = [Product]
admin.site.register(tables)
```

### 9. Register the smartphone's app to the django's project
`config/settings.py`
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # APPS
    'api.apps.ApiConfig',
]
```

### 10. make migration DB Schema
```bash
python manage.py makemigrations
```

### 11. migrate DB
```bash
python manage.py migrate
```


## Create The Views of API
### 1. Create the view of the products
`api/view.py`
```python
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
```
`config/urls.py`
```python
from api.views import get_products

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/products/', get_products),
]
```

### 2. Create the get a product
`api/views.py`
```python
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
```
`config/urls.py`
```python
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/products/', get_products),
    path('api/product/<int:id>', get_product),
]
```

### 3. Add product api
`api/views.py`
```python
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
```
`config/settings.py`
```python
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
```

### 4. Create update view
`api/views.py`
```python
def update_product(request: HttpRequest, id: int) -> JsonResponse:
    if request.method == 'POST':
        data = request.POST
        product = Product.objects.get(id=id)
        if data.get('name') is not None:
            product.name    = data['name']
        if data.get('company') is not None:
            product.company = data['company']
        if data.get('color') is not None:
            product.color   = data['color']
        if data.get('RAM') is not None:
            product.RAM     = data['RAM']
        if data.get('memory') is not None:
            product.memory  = data['memory']
        if data.get('price') is not None:
            product.price   = data['price']
        if data.get('img_url') is not None:
            product.img_url = data['img_url']
        product.save()

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
```
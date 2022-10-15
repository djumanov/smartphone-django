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
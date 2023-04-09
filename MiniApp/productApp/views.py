from django.shortcuts import render

# Create your views here.

def electronics(request):
    productDict={
        'product1': 'Mac',
        'product2': 'Iphone',
        'product3': 'Dell',
    }
    return render(request, 'productApp/products.html', productDict)

def toys(request):
    productDict={
        'product1': 'Remote Car',
        'product2': 'Drone',
        'product3': 'Rocket Launcher',
    }
    return render(request, 'productApp/products.html', productDict)

def shoes(request):
    productDict={
        'product1': 'Nike',
        'product2': 'Adidas',
        'product3': 'Acsis',
    }
    return render(request, 'productApp/products.html', productDict)

def index(request):
    return render(request, 'productApp/index.html')
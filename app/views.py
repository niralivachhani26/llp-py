from django.shortcuts import render
from django.http import JsonResponse

def get_main_menu(request):
    base_url = "http://127.0.0.1:8000/"
    menu = [
        {"name": "Home", "url": "/"},
        {"name": "About Us", "url": "/about"},
        {"name": "Services", "url": "/services"},
        {"name": "Projects", "url": "/projects"},
        {"name": "Clients", "url": "/clients"},
        {"name": "Blogs", "url": "/blogs"},
        {"name": "Careers", "url": "/careers"},
        {"name": "Contact Us", "url": "/contact"},
    ]

    full_menu = [
        {"name": item["name"], "url": base_url.rstrip("/") + item["url"]}
        for item in menu
    ]

    return JsonResponse(full_menu, safe=False)

def index(request):
    banners = [
        {'image_url': 'images/banner1.png'},
        {'image_url': 'images/banner2.png'},
        {'image_url': 'images/banner3.png'},
    ]
    return JsonResponse(banners, safe=False)

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def projects(request):
    return render(request, 'projects.html')

def clients(request):
    return render(request, 'clients.html')

def blogs(request):
    return render(request, 'blogs.html')

def careers(request):
    return render(request, 'careers.html')

def contact(request):
    return render(request, 'contact.html')
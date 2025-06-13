from django.shortcuts import render
<<<<<<< HEAD
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

=======
from .models import Section8

def chunked(iterable, chunk_size):
    return [iterable[i:i + chunk_size] for i in range(0, len(iterable), chunk_size)]

def home_view(request):
    return render(request, 'home.html')

def section8_view(request):
    testimonials = Section8.objects.all()
    return render(request, 'section8.html', {'testimonials': testimonials})

def section10_view(request):
    return render(request, 'section10.html')

def about_view(request):
    return render(request, 'about.html')

def services_view(request):
    return render(request, 'services.html')

def services_detail(request):
    return render(request, 'services_detail.html')

>>>>>>> homepage_section8_10_new
def projects(request):
    return render(request, 'projects.html')

def clients(request):
    return render(request, 'clients.html')

<<<<<<< HEAD
def blogs(request):
    return render(request, 'blogs.html')
=======
def blog(request):
    return render(request, 'blog.html')
>>>>>>> homepage_section8_10_new

def careers(request):
    return render(request, 'careers.html')

def contact(request):
<<<<<<< HEAD
    return render(request, 'contact.html')
=======
    return render(request, 'contact.html')

def outdoor_signage(request):
    return render(request, 'outdoor_signage.html')

def indoor_signage(request):
    return render(request, 'indoor_signage.html')

def digital_signage(request):
    return render(request, 'digital_signage.html')

def led_displays(request):
    return render(request, 'led_displays.html')

def vehicle_graphics(request):
    return render(request, 'vehicle_graphics.html')

def vinyl_stickers(request):
    return render(request, 'vinyl_stickers.html')

def large_format_printing(request):
    return render(request, 'large_format_printing.html')

def custom_acrylic_branding(request):
    return render(request, 'custom_acrylic_branding.html')












>>>>>>> homepage_section8_10_new

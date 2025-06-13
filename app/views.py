from django.shortcuts import render
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

def projects(request):
    return render(request, 'projects.html')

def clients(request):
    return render(request, 'clients.html')

def blog(request):
    return render(request, 'blog.html')

def careers(request):
    return render(request, 'careers.html')

def contact(request):
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













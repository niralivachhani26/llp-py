from django.shortcuts import render
from .models import Section8

def chunked(iterable, chunk_size):
    return [iterable[i:i + chunk_size] for i in range(0, len(iterable), chunk_size)]
def index(request):
    testimonials = Section8.objects.all()
    return render(request, 'index.html', {'testimonials': testimonials})


from django.shortcuts import render
from .models import Service

# Create your views here.

def services(request):
    # return HttpResponse('<h1>Servicios</h1><h2>Esta es la página de servicios')
    services = Service.objects.all()
    return render(request, 'services/services.html', {'services': services})

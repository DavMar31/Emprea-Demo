from django.shortcuts import render #, HttpResponse

# Create your views here.
def home(request):
    # return HttpResponse('<h1>Inicio</h1><h2>Esta es la página de inicio')
    return render(request, 'core/home.html')

def about(request):
    # return HttpResponse('<h1>Acerca de</h1><h2>Esta es la página acerca de:')
    return render(request, 'core/about.html')

def store(request):
    # return HttpResponse('<h1>Tienda</h1><h2>Esta es la página de la Tienda')
    return render(request, 'core/store.html')

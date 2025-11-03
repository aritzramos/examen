from django.shortcuts import render
from django.views.defaults import page_not_found

# Create your views here.

# Errores

def mi_error_404(request,exception=None):
    return render(request, 'errores/404.html',None,None,404)

def mi_error_400(request,exception=None):
    return render(request, 'errores/400.html',None,None,400)

def mi_error_403(request,exception=None):
    return render(request, 'errores/403.html',None,None,403)

def mi_error_500(request,exception=None):
    return render(request, 'errores/500.html',None,None,500)

# Index
def index(request):
    return render(request, 'app/index.html')

# Querys


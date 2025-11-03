"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

handler404 = 'app.views.mi_error_404'
handler400 = 'app.views.mi_error_400'
handler403 = 'app.views.mi_error_403'
handler500 = 'app.views.mi_error_500'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('__debug__/',include("debug_toolbar.urls")),
    path('', include('app.urls')),
]

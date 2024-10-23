"""
URL configuration for main_prototyper project.

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
from django.urls import path , include

# importing our static from conf #
from django.conf.urls.static import static

#importing our settings from conf #
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('prototype/',include('app_prototype.urls'))
    
    #this will help us to handle media files and documents #
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

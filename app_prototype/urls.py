

from django.contrib import admin
from django.urls import path , include

# importing our static from conf #
from django.conf.urls.static import static

#importing our settings from conf #
from django.conf import settings
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),

    path('',views.index,name='index')
    
    #this will help us to handle media files and documents #
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

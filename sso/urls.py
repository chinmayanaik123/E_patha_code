
from django.contrib import admin
from django.urls import path, include 
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',TemplateView.as_view(template_name='dashboard/home.html'),name='home'),
    path('accounts/', include('allauth.urls')),  
    path('e_patha/', include('e_patha.urls'),name='e_patha'),
    path('tourism/', include('tourism.urls')),
    path('temple/', include('temple.urls')),
    path('local_shop/', include('local_shop.urls')),
    path('', views.home),
    path('contacts/', include('contacts.urls')) 
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


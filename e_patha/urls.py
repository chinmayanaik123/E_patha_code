from django.urls import path
from . import views
 
urlpatterns = [
    path("", views.index1, name="index1"), 
    path("index1/", views.index1, name="index1"), 
    path("about/", views.about, name="about"),
    path("Contact_us_/", views.Contact_us_, name="Contact_us_"), 

    path("weather/",views.weather,name='weather'),
    path('gallery/',views.gallery,name='gallery'),

    path('Bus_Timmings/',views.Bus_Timmings,name='Bus_Timmings'),
    path('map/',views.map,name='map'),

    path('donation/',views.donation,name='donation'),
    path('panchayath/',views.panchayath,name='panchayath'),
    path('indexx/',views.indexx,name='indexx'),
  
 
] 

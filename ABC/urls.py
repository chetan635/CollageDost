from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name="MainHome"),
    path("contact/",views.contact,name="AboutUs"),
    path("IIT/",views.IIT,name="IIT"),
    path("NIT/",views.NIT,name="NIT"),
    path("IIT2/",views.IIT2,name="IIT2"),
    path("NIT2/",views.NIT2,name="NIT2"),
    path("IIIT/",views.IIIT,name="NIT2"),
    path("IIIT2/",views.IIIT2,name="NIT2"),
    path("JEE/",views.JEE,name="JEE"),
    path("JEE2/",views.JEE2,name="JEE2"),
    
  
    
]
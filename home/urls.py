from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('services/',views.services,name='services'),
    path('contact/',views.contact,name='contact'), 
    path('save/',views.save,name='save'),


]


from django.contrib import admin
from django.http.response import HttpResponse
from django.urls import path
from . import views;

urlpatterns = [
    path('admin/', admin.site.urls),
    path('customers/<int:id>',views.customers,name='customers.show'),
    path('products/',views.products,name='products'),
    path('',views.dashboard,name='dashboard')
]

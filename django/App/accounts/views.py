from django.shortcuts import render
from django.http.response import HttpResponse
from accounts.models import *

# Create your views here.
def customers(request,id):
    customer=Customer.objects.get(id=id)
    orders=customer.order_set.all()
    order_count=orders.count()
    return render(request,'accounts/customers.html',{
        'customers':customer,
        'orders':orders,
        'order_count':order_count
    })

def products(request):
    products=Product.objects.all()
    return render(request,'accounts/products.html',{
        'products':products
    })

def dashboard(request):
    customer=Customer.objects.all()
    orders=Order.objects.all()
    total=orders.count()
    delivered=Order.objects.filter(status="delivered").count()
    pending=Order.objects.filter(status="pending").count()
    return render(request,'accounts/dashboard.html',{
        'customers':customer,
        'orders':orders,
        'total':total,
        'delivered':delivered,
        'pending':pending
    })
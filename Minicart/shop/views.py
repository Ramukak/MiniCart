from django.shortcuts import render,HttpResponse
from .models import *
from django.db.models import Q
# Create your views here.
def indexView(request):
    return render(request,"home.html")

def itemView(request):
    products = Product.objects.all()
    context = {'products':products}
    return render(request,'shop.html',context)

def searchProduct(request):
    query = request.GET.get('q')
    if query:
        products = Product.objects.filter(Q(title__icontains=query) | Q(desc__icontains=query))
    else:
        products = Product.objects.all()
    context = {'products':products} 
    return render(request,'shop.html',context)

from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from .models import *
import json
from django.contrib.auth.forms import UserCreationForm  
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
# Create your views here.
def detail(request):
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer=customer,complete = False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items

    else:
        items = []
        cartItems = 0
        order = {'get_cart_items':0,'get_order_total':0}
    id = request.GET.get('id','')
    products = Product.objects.filter(id=id)
    context = {'products':products,'items': items,'order': order,'cartItems': cartItems}
    return render(request,'pages/products/detail.html',context)

def category(request):
    categories = Category.objects.filter(is_sub = False)
    active = request.GET.get('category','')
    if active:
        products = Product.objects.filter(category__slug = active) 

    context= {'id':id,'categories': categories,'products': products,'active': active}
    return render(request,'pages/products/category.html',context)
def search(request):
    if request.method == 'POST':
         searched = request.POST["searched"]
         keys = Product.objects.filter(name__contains = searched)
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer=customer,complete = False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_items':0,'get_order_total':0}
        cartItems = order['get_cart_items']
    categories = Category.objects.filter(is_sub = False)
    products = Product.objects.all()
    return render(request, 'pages/products/search.html',{'categories':categories,'searched':searched, 'keys':keys,'products': products,'cartItems': cartItems})

def register(request):
    form = UserForm()    
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    context ={'form': form}
    return render(request, 'pages/accounts/register.html',context)
def logoutPage(request):
    logout(request)
    return redirect('home')

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.info(request, 'Username or password is incorrect')
    context = {}
    return render(request, 'pages/accounts/login.html', context)
def index(request):     
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer=customer,complete = False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        cartItems = []
        order = {'get_cart_items':0,'get_order_total':0}
        cartItems = order['get_cart_items']
    categories = Category.objects.filter(is_sub = False)
    products = Product.objects.all()
    context = {'categories':categories, 'products': products,'cartItems': cartItems}  
    return render(request, 'pages/home.html',context)
def products(request):
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer=customer,complete = False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        cartItems = []
        order = {'get_cart_items':0,'get_order_total':0}
        cartItems = order['get_cart_items']
    categories = Category.objects.filter(is_sub = False)
    products = Product.objects.all()
    context = {'categories':categories, 'products': products,'cartItems': cartItems}    
    return render(request, 'pages/products/products.html',context)

def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    customer = request.user
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer,complete = False)
    orderItem, created = OrderItem.objects.get_or_create(order=order,product = product)
    if action == 'add':
        orderItem.quantity += 1
    elif action == 'remove':
        orderItem.quantity -= 1
    orderItem.save()
    if orderItem.quantity<= 0:
        orderItem.delete()
    return JsonResponse('address',safe=False,)
def cart(request):
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer=customer,complete = False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items

    else:
        items = []
        cartItems = 0
        order = {'get_cart_items':0,'get_order_total':0}
    context = {'items': items,'order': order,'cartItems': cartItems}
    return render(request, 'pages/products/cart.html', context)
def checkout(request):
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer=customer,complete = False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        cartItems = []

        order = {'get_cart_items':0,'get_order_total':0}
    context = {'items': items,'order': order,'cartItems': cartItems}
    return render(request, 'pages/products/checkout.html',context)

from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render,redirect
from django.forms import BaseModelForm
from mainapp.forms import AddtocartForm
from django.views import View
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from mainapp.models import Products,AddtoCart,Order
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.views.generic import DetailView,TemplateView,ListView
# Create your views here.
class HomeView(TemplateView):
    template_name='Hom.html'

def RegView(request):
    if request.method=='POST':
        Username=request.POST['username']
        Email=request.POST['email']
        Password=request.POST['password']
        Firstname=request.POST['firstname']
        Lastname=request.POST['lastname']
        if User.objects.filter(username=Username).exists():
            messages.info(request,'username already exist')
            return redirect('reg_view')
        elif User.objects.filter(email=Email).exists():
            messages.info(request,' email already exit')
            return redirect('reg_view')
        else:
            user=User.objects.create_user(username=Username,email=Email,password=Password,first_name=Firstname,last_name=Lastname)
            user.save()
        return redirect("log_view")
    else:
        return render(request,'Register.html')
    
def LoginView(request):
    if request.method=='POST':
        Username=request.POST['username']
        Password=request.POST['password']
        user=authenticate(username=Username,password=Password)
        if user:
            login(request,user)
            return redirect('product_view')
        else:
            messages.info(request,'inavlid credentials')
            return redirect('log_view')
    else:
        return render(request,'login.html')
    
def LogoutView(request):
    logout(request)
    return redirect('home_view')

class IndexView(TemplateView):
    template_name='index.html'

def ProductView(request):
    products=Products.objects.all()
    return render(request,'index.html',{'product':products})
class CateogryView(View):
    def get(self,request,val):
        products=Products.objects.filter(cateogry=val)
        return render(request,'cateogry.html',locals())
    
class ProductdetailView(DetailView):
    model=Products
    template_name='detail.html'
    context_object_name='products'
    pk_url_kwarg='id'

class AddtocartView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get('id')
        product=Products.objects.get(id=id)
        form=AddtocartForm()
        return render(request,'Addtocart.html',{'form':form,'product':product})
    def post(self,request,*args,**kwargs):
        id=kwargs.get('id')
        product=Products.objects.get(id=id)
        user=request.user
        quantity=request.POST['quantity']
        res=AddtoCart.objects.filter(user=request.user,product=product,status='in-cart').first()
        if res:
          
               
        
                res.quantity += int(quantity)
                res.save()
                return redirect('cart_view')

        else:
            AddtoCart.objects.create(user=user,product=product,quantity=quantity,status='in-cart')
            return redirect('cart_view')
       
class  CartListView(ListView):
    template_name='showcart.html'  
    model=AddtoCart  
    context_object_name='cart'
      

    def get_queryset(self):
        return AddtoCart.objects.filter(user=self.request.user).exclude(status="order-placed")
class CartdeleteView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get('id')
        cartitem=AddtoCart.objects.get(id=id)
        cartitem.delete()
        return redirect('cart_view')
class PlaceorderView(View):
    def get(self,request,*args,**kwargs):
        return render(request,'placeorder.html')
    
    def post(self,request,*args,**kwargs):
        user=request.user
        cid=kwargs.get('cid')
        pid=kwargs.get('pid')
        product=Products.objects.get(id=pid)
        name=request.POST['name']
        email=request.POST['email']
        address=request.POST['address']
        Order.objects.create(user=user,Product=product,name=name,email=email,address=address)
        cart=AddtoCart.objects.get(id=cid)
        cart.status="order-placed"
        cart.save()
        return redirect('order_view')
    
class OrderlistView(ListView):
    model=Order
    template_name='oderlist.html'
    context_object_name='order'


    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)
    
class OrderdeleteView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get('id')
        order_item=Order.objects.get(id=id)
        order_item.delete()
        return redirect('order_view')
    





    

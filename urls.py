"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from mainapp import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.HomeView.as_view(),name='home_view'),
    path('reg',views.RegView,name='reg_view'),
    path('log',views.LoginView,name='log_view'),
    path('logout',views.LogoutView,name='logout_view'),
    path('product',views.ProductView,name='product_view'),
    path('cat/<slug:val>',views.CateogryView.as_view(),name='cateogry_view'),
    path('detail/<int:id>',views.ProductdetailView.as_view(),name='detail_view'),
    path('Addcart/<int:id>',views.AddtocartView.as_view(),name="addcart_view"),
    path('showcart',views.CartListView.as_view(),name="cart_view"),
    path('Del/<int:id>',views.CartdeleteView.as_view(),name="deletecart_view"),
    path('order/<int:cid>/<int:pid>',views.PlaceorderView.as_view(),name="placeorder_view"),
    path('orderlist',views.OrderlistView.as_view(),name="order_view"),
    path('Delorder/<int:id>',views.OrderdeleteView.as_view(),name="deleteorder_view"),

  




    
   

    







    

    
    

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

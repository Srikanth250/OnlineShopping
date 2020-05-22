"""OnlineShopping URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from Ekart.views import signup, signin, logout, homePage, mobiles, laptops, dslrs, productDesc_cart_checkout_ack_page

urlpatterns = [
    path('admin/', admin.site.urls),
	path('signup/', signup),
	path('login/', signin),
	path('mobiles/', mobiles),
	path('laptops/', laptops),
	path('dslrs/', dslrs),
	path('products/<str:name>/<int:no>/<str:itype>/', productDesc_cart_checkout_ack_page),
	path('home/', homePage),
	path('logout/', logout)
]

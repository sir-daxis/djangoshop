from django import views
from django.contrib import admin
from django.urls import path

from .views.home import Index, store
from .views.singup import Singup
from .views.login import Login, logout
from .views.cart import Cart
from .views.checkout import CheckOut
from .views.orders import OrderView
from .middlewares.auth import auth_middleware

urlpatterns = [
    path('', Index.as_view(), name='homepage'),
    path('store', store, name='store'),
    path('singup', Singup.as_view(), name='singup'),
    path('login', Login.as_view(), name='lofgin'),
    path('cart', CheckOut.as_view(), name='checkout'),
    path('orders', auth_middleware(OrderView.as_view()), name='orders'),
]
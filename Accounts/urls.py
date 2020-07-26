from django.urls import path
from .views import *
from . import *

urlpatterns = [
    path('login/',login_view),
    path('signup/',register_view,name='signup'),
    path('logout/',logout_view),
    path('productview/<int:myid>', Productview.as_view(),name='product_detail'),
    path('womens/',Womensview.as_view(), name='womens'),
    path('mens/',Mensview.as_view(), name='mens'),
    path('accessories/',Accessoriesview.as_view(), name='mens'),
    path('womenproductview/<int:myid>', WomenProductview.as_view(),name='womenproduct_detail'),
    path('menproductview/<int:myid>', MenProductview.as_view(),name='menproduct_detail'),




]

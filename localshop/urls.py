from django.urls import path, include
from rest_framework import routers
from . import views


app_name = 'localshop'


router = routers.DefaultRouter()
router.register('product', views.ProductView)



urlpatterns = [
    path('', views.all_products, name='all_products'),
    path('item/<slug:slug>/', views.product_detail, name='product_detail'),
    path('search/<slug:category_slug>', views.category_list, name='category_list'),
    path('', include(router.urls)),
   
    
   
    
    

]
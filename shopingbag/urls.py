from django.urls import path

from . import views


app_name = 'shopingbag'


urlpatterns = [ 
    path('', views.shopingbag_summary, name='shopingbag_summary'),

    
    

]
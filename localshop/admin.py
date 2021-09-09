from django.contrib import admin
from .models import Category, Product



@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'category','author','slug','price']

    prepopulated_fields = {'slug':('title',)}





@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

                
    

    prepopulated_fields = {'slug':('name',)}
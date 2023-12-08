from django.contrib import admin

from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug'] # telling django the fields to show in the list
    prepopulated_fields = {'slug': ('name',)} #slugfield gets populated when something is typed into the name


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'brand', 'slug', 'price',
                    'in_stock', 'created', 'updated'] 
    list_filter = ['in_stock', 'is_active'] #to be able to filter the list 
    list_editable = ['price', 'in_stock'] #to edit the price and items in stock
    prepopulated_fields = {'slug': ('title',)} #slugfield gets populated when something is typed into the title

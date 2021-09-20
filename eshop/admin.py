from django.contrib import admin
from .models import Customer,Product,Orders,Feedback
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
# Register your models here.
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display=('user','address','mobile','thumbnail_preview')

    def thumbnail_preview(self,obj):
        return obj.thumbnail_preview
    thumbnail_preview.short_description="Customer Image "
    thumbnail_preview.allow_tags=True

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display=('name','price','thumbnail_preview')
    list_editable=('price',)
    def thumbnail_preview(self,obj):
        return obj.thumbnail_preview
    thumbnail_preview.short_description="Product Image "
    thumbnail_preview.allow_tags=True
@admin.register(Orders)
class OrderAdmin(admin.ModelAdmin):
    list_display=('Customer','product','email','status','order_date')
    list_editable=('status',)
    list_filter=('order_date',)
@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display=('name','feedback','date')

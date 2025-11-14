from django.contrib import admin
from .models import ServiceType

@admin.register(ServiceType)
class ServiceTypeAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
list_display = ('name', 'subtitle', 'order')
from django.contrib import admin

# Register your models here.

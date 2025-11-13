from django.contrib import admin
from .models import ServiceType

@admin.register(ServiceType)
class ServiceTypeAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

from django.contrib import admin

# Register your models here.

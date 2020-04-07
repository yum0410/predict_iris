from django.contrib import admin
from .models import Iris

@admin.register(Iris)
class IrisAdmin(admin.ModelAdmin):
    pass

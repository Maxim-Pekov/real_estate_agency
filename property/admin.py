from django.contrib import admin

from .models import Flat


@admin.register(Flat)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('town', 'address', 'owner')
    search_fields = ('town', 'address', 'owner')


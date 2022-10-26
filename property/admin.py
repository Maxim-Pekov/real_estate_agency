from django.contrib import admin
from .models import Flat


@admin.register(Flat)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('address', 'price', 'new_building', 'construction_year', 'town')
    list_editable = ('new_building',)
    search_fields = ('town', 'address', 'owner', 'new_building')
    readonly_fields = ["created_at"]


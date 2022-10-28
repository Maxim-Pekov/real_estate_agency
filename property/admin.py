from django.contrib import admin
from .models import Flat, Сomplaint


@admin.register(Flat)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('address', 'price', 'new_building', 'construction_year', 'town')
    list_editable = ('new_building',)
    list_filter = ('new_building',)
    search_fields = ('town', 'address', 'owner', 'new_building')
    readonly_fields = ["created_at"]
    raw_id_fields = ('liked_by',)


@admin.register(Сomplaint)
class CategoryAdmin(admin.ModelAdmin):
    # list_display = ('user', 'сomplaint_text')
    raw_id_fields = ('flat', 'user')


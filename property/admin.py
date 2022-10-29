from django.contrib import admin
from .models import Flat, Сomplaint, Owner


class FlatsOwners(admin.TabularInline):
    model = Flat.owners.through
    raw_id_fields = ('owner',)


@admin.register(Flat)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('address', 'price', 'new_building', 'construction_year')
    list_editable = ('new_building',)
    list_filter = ('new_building',)
    search_fields = ('town', 'address', 'owner', 'new_building')
    readonly_fields = ["created_at"]
    raw_id_fields = ('liked_by',)
    inlines = [FlatsOwners]


@admin.register(Сomplaint)
class CategoryAdmin(admin.ModelAdmin):
    # list_display = ('user', 'сomplaint_text')
    raw_id_fields = ('flat', 'user')


@admin.register(Owner)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('owner', 'owners_phonenumber', 'owner_pure_phone')
    raw_id_fields = ('owned_apartments',)

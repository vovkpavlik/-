from django.contrib import admin

from .models import Flat
from .models import Complaint
from .models import Owner


class OwnedFlatInline(admin.TabularInline):
    model = Flat.owned.through

    raw_id_fields = (
    "owner",
    )

@admin.register(Flat)
class FlatAdmin(admin.ModelAdmin):
    
    inlines = [
        OwnedFlatInline,
    ]

    search_fields = ("town", "address", "owner")

    readonly_fields = ["created_at"]

    list_display = (
    "address",
    "price",
    "new_building",
    "construction_year",
    "town",
    )

    list_filter = ["new_building"]

    raw_id_fields = ("who_liked",)


@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    list_display = (
    "complaint_text",
    )
   
    raw_id_fields = (
        "who_complained",
        "flat_number",
    )


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    list_display = (
    "full_name",
    "owners_phonenumber",
    "owner_pure_phone",
    )

    raw_id_fields = (
        "flats",
    )

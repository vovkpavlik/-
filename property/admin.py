from django.contrib import admin

from .models import Flat
from .models import Complaint


class FlatAdmin(admin.ModelAdmin):
    search_fields = ("town", "address", "owner")

    readonly_fields = ["created_at"]

    list_display = (
    "address",
    "price",
    "new_building",
    "construction_year",
    "town",
    "owner_pure_phone"
    )

    list_filter = ["new_building"]

    raw_id_fields = ("who_liked",)


class ComplaintAdmin(admin.ModelAdmin):
    list_display = (
    "complaint_text",
    )
   
    raw_id_fields = (
        "who_complained",
        "flat_number",
    )


admin.site.register(Flat, FlatAdmin)
admin.site.register(Complaint, ComplaintAdmin)

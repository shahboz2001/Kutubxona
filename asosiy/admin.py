from django.contrib import admin
# Register your models here.
from .models import *


# admin.site.register(Muallif)
@admin.register(Muallif)
class MuallifAdmin(admin.ModelAdmin):
    list_display=("id","ism","tirik","kitob_soni","jinsi","tugulgan_sana")
    list_display_links = ("id","ism")
    list_editable = ("kitob_soni","tirik")
    search_fields = ("id","ism")
    search_help_text = "id, ism qidiruv"
    list_filter = ("tirik",)
    list_per_page = 6
# admin.site.register(Talaba)
@admin.register(Talaba)
class TalabaAdmin(admin.ModelAdmin):
    list_display = ("id", "ism", "kurs", "kitoblar_soni", "bitiruvchi", "kurs")
    list_display_links = ("id", "ism")
    list_editable = ("kurs", "kitoblar_soni", "bitiruvchi")
    list_filter = ("bitiruvchi",)
    list_per_page = (5)
    search_fields = ("id", "ism", "kitoblar_soni")
    search_help_text = "id, ism, kitoblar soni boyivha qidiruv bering"


# admin.site.register(Admin)
@admin.register(Admin)
class AdminAdmin(admin.ModelAdmin):
    list_filter = ("ish_vaqti",)
    search_fields = ("ism","ish_vaqti")
    list_per_page = 5
# admin.site.register(Kitob)
@admin.register(Kitob)
class KitobAdmin(admin.ModelAdmin):
    search_fields = ("id",)

# admin.site.register(Record)
@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
    autocomplete_fields = ("telaba", "kitob", "admin")
    list_display = ("id","telaba","kitob","admin","olingan_sana","qayterdi")
    search_fields = ("id",)



# admin.site.register(Nashriyot)
# admin.site.register(Kitob1)
# admin.site.register(Sotuvchi)
# admin.site.register(Sotuv)

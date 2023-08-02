from django.contrib import admin
from .models import *

@admin.register(Urunler)
class UrunlerAdmin(admin.ModelAdmin):
    list_display = ('title','category','puan','user','id')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title','slug','id')

@admin.register(Renk)
class RenkAdmin(admin.ModelAdmin):
    list_display = ('title','slug','id')

@admin.register(BedenAyakkabi)
class BedenAyakkabiAdmin(admin.ModelAdmin):
    list_display = ('urun','renk','beden','stok','id')

@admin.register(BedenKiyafet)
class BedenKiyafetAdmin(admin.ModelAdmin):
    list_display = ('urun','renk','stok','beden','id')

@admin.register(UrunStok)
class UrunStokAdmin(admin.ModelAdmin):
    list_display = ('urun','id')

@admin.register(UrunImg)
class UrunImgAdmin(admin.ModelAdmin):
    list_display = ('urun','id')

@admin.register(Beden)
class BedenAdmin(admin.ModelAdmin):
    list_display = ('title','id')

@admin.register(Beden2)
class Beden2Admin(admin.ModelAdmin):
    list_display = ('title','id')

@admin.register(Shopbasket)
class ShopbasketAdmin(admin.ModelAdmin):
    list_display = ('user','product_letter','price_all','count','id')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user','product','star','date_now','id')


    
    
    
    

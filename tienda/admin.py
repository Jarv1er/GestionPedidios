from django.contrib import admin
from .models import CategoriaProd, Producto

# Register your models here.

class CategoriaProAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "update")


class ProductoAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "update")


admin.site.register(CategoriaProd, CategoriaProAdmin)
admin.site.register(Producto, ProductoAdmin)
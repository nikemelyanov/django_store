from django.contrib import admin

from products.models import ProductCategory, Product, Basket

admin.site.register(ProductCategory)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'category')
    fields = ('category', 'name', 'description', ('price', 'quantity'), 'image')
    search_fields = ('name',)
    ordering = ('name',)
    # readonly_fields = 
 
    
class BasketAdmin(admin.TabularInline):
    model = Basket
    fields = ('product', 'quantity', 'created_timestamp')
    readonly_fields = ('created_timestamp',)
    extra = 0
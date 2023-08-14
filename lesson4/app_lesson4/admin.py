from django.contrib import admin
from .models import Advertisement

class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'price', 'create_at', 'auction', 'created_date', 'updated_date', 'image_img']
    list_filter = ['auction','create_at']
    actions = ['make_auction_as_false', 'make_auction_as_true']
    fieldsets = (
        ('О товаре', {
            'fields': ('title', 'description', 'image'),
        }),
        ('Цена товара', {
            'fields': ('price','auction'),
            'classes':['collapse']
        })
    )

    @admin.action(description='убрать возможность торга')
    def make_auction_as_false(self, request, queryset):
        queryset.update(auction = False)

    @admin.action(description='Добавить возможность торга')
    def make_auction_as_true(self, request, queryset):
        queryset.update(auction = True)

admin.site.register(Advertisement, AdvertisementAdmin)
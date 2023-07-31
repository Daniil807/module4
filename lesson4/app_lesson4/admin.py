from django.contrib import admin
from .models import Advertisement

class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'price', 'create_at', 'auction']

admin.site.register(Advertisement, AdvertisementAdmin)
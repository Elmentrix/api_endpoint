from django.contrib import admin
from .models import items


class itemAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'image', 'created_on')

admin.site.register(items, itemAdmin)

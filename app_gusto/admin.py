from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Special)
@admin.register(models.Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ['title','price','menu_section_title']
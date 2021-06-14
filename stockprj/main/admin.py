from django.contrib import admin
from .models import New
# Register your models here.

@admin.register(New)
class NewAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'aurthor', 'publish', 'status')
    list_filter = ('status', 'publish', 'aurthor')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('aurthor',)
    date_hierarchy = 'publish'
    ordering = ('status', 'publish')
    
    
    

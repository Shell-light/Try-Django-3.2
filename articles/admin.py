from django.contrib import admin

# Register your models here.
from .models import Article

class ArticelAdmin(admin.ModelAdmin):
    list_display = ['id','title', 'timestamp', 'updated']
    search_fields = ['title', 'content']

admin.site.register(Article, ArticelAdmin)
from django.contrib import admin
from .models import Blog, BlogCategory


class BlogAdmin(admin.ModelAdmin):
    pass

admin.site.register(Blog)
admin.site.register(BlogCategory)

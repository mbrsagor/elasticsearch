from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'order', 'slug')


admin.site.register(Post, PostAdmin)

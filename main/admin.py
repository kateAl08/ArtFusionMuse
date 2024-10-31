from django.contrib import admin
from .models import Art, Category, Post, Snippet

# Register your models here.
admin.site.register(Art)
admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Snippet)

# Customize admin interface

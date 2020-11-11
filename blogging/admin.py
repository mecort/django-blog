from django.contrib import admin
from blogging.models import Post, Category

# class CategoryAdmin(admin.ModelAdmin):
#     # Fill me

# class PostAdmin(admin.ModelAdmin):
#     # Fill me

admin.site.register(Post)
admin.site.register(Category)

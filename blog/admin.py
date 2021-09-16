
from django.contrib import admin
from blog.models import Post, Comment, Like
from category.models import Category


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ['author', 'title', 'image_front', 'image', 'activate_date', 'due_date', 'is_activate']


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment)
admin.site.register(Like)

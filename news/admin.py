from django.contrib import admin
from .models import Post, Category, Author


class PostAdmin(admin.ModelAdmin):
    list_display = ('header', 'authorArticle', 'creationTime',)
    list_filter = ('header', 'creationTime', 'authorArticle',)
    search_fields = ('header', 'textCategory__categoryName',)

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('account', 'ratingAuthor',)
    list_filter = ('account', 'ratingAuthor',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('categoryName',)
    list_filter = ('categoryName',)

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Author, AuthorAdmin)

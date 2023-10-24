"""Django models utilities."""
from django.contrib import admin
from django.utils.html import format_html

# Models
from .models import Post, Category, Tag


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Post admin."""

    list_display = ('title', 'author', 'published', 'display_image')
    ordering = ('author', 'published')
    search_fields = ('title', 'author__username', 'categories__name', 'tags__name')
    list_filter = ('author__username', 'categories__name', 'tags__name', 'published')
    prepopulated_fields = {'slug': ('title',)}

    def display_image(self, obj):
        """Display image."""
        if obj.image:
            return format_html('<img src="{}" width="50" height="50" />', obj.image.url)
        else:
            return 'Sin Imagen'

    display_image.short_description = 'Vista previa de la imagen'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Category admin."""

    list_display = ('name', 'created', 'modified')
    ordering = ('name',)
    search_fields = ('name', 'description')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    """Tag admin."""

    list_display = ('name', 'slug', 'created', 'modified')
    prepopulated_fields = {'slug': ('name',)}

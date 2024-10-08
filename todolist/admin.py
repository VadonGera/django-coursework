from django.contrib import admin

from .models import Task, Comment, Tag, Category


class CommentInLine(admin.TabularInline):
    model = Comment


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'owner', 'due_date', 'status', 'is_active',)
    list_filter = ('owner', 'category', 'status', 'is_active',)
    search_fields = ('title', 'description',)
    ordering = ('-due_date',)

    inlines = [CommentInLine]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'color',)
    search_fields = ('name',)
    ordering = ('name',)


admin.site.register(Tag)

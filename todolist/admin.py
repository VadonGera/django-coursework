from django.contrib import admin

from .models import Task, Comment, Tag, Category


# admin.site.register(Task)


class CommentInLine(admin.TabularInline):
    model = Comment


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'owner', 'due_date', 'status',)
    list_filter = ('owner', 'category', 'status',)
    search_fields = ('title', 'description',)
    ordering = ('-due_date',)

    inlines = [CommentInLine]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'color',)
    search_fields = ('name',)
    ordering = ('name',)


admin.site.register(Tag)

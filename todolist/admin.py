from django.contrib import admin

from todolist.models import Tag, Task


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    search_fields = ("name",)


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    search_fields = ("content",)
    list_display = ("content", "deadline", "is_completed")
    list_filter = ("is_completed",)

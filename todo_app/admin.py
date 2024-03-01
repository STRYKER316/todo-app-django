from django.contrib import admin
from todo_app.models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display = ('description', 'is_completed', 'created_at', 'updated_at')
    list_filter = ('is_completed', 'created_at', 'updated_at')
    search_fields = ('description',)


# Register your models here.
admin.site.register(Task, TaskAdmin)
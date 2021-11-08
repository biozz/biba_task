from django.contrib import admin
from .models import Task


class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'status', 'description')

admin.site.register(Task, TaskAdmin)
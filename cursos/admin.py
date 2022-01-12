from django.contrib import admin

from .models import Course, Avaliation

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'url', 'created_at', 'updated_at', 'active']
    list_display_links = ['id', 'title', 'url']
    search_fields = ['title', 'url']
    list_filter = ['created_at', 'updated_at', 'active']

@admin.register(Avaliation)
class AvaliationAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'course', 'rate', 'created_at', 'updated_at', 'active']
    list_display_links = ['id', 'name', 'email', 'course', 'rate']
    search_fields = ['name', 'email', 'course', 'rate']
    list_filter = ['created_at', 'updated_at', 'active']

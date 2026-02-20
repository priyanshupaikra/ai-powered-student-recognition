from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'enrollment_number', 'room_number', 'course', 'created_at')
    search_fields = ('name', 'enrollment_number', 'room_number')
    list_filter = ('course', 'created_at')
    ordering = ('name',)
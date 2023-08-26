from django.contrib import admin

# Register your models here.
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'cnic', 'gender', 'city', 'state', 'country')
    search_fields = ('name', 'cnic',)
    list_filter = ('gender', 'city', 'state', 'country')
from django.contrib import admin

from .models import Course, Category, Entry

# Register your models here.
admin.site.register(Course)
admin.site.register(Category)
admin.site.register(Entry)

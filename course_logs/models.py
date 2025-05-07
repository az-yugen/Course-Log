from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Course(models.Model):
    """courses here"""
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.CharField(max_length=200)

    def __str__(self):
        return self.course


class Category(models.Model):
    """categories here"""
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.category


class Entry(models.Model):
    """log entries for particular course and category here"""
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    date = models.DateField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date']
        verbose_name_plural = 'entries'

    def __str__(self):
        return f"{self.description[0:100]}..."
    

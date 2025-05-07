"""defining url patterns for course_logs"""

from django.urls import path
from . import views

app_name = 'course_logs'
urlpatterns = [
    # home page
    path('', views.home, name='home'),


    # page showing all courses defined
    path('all_courses/', views.all_courses, name='all_courses'),
    # page showing all categories defined
    path('all_categories/', views.all_categories, name='all_categories'),


    # page showing all entries with same course
    path('this_course/<int:course_id>/', views.this_course, name='this_course'),
    # page showing all entries with same category
    path('this_category/<int:category_id>/', views.this_category, name='this_category'),
    # page showing this particular entry in detail
    path('this_entry/<int:entry_id>/', views.this_entry, name='this_entry'),


    # page for adding new course
    path('new_course/', views.new_course, name='new_course'),
    # page for adding new category
    path('new_category/', views.new_category, name='new_category'),
    # page for adding new entry
    path('new_entry/', views.new_entry, name='new_entry'),


]

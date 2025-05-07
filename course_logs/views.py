from django.shortcuts import render, redirect

from .models import Course, Category, Entry
from .forms import CourseForm, CategoryForm, EntryForm
from django.contrib.auth.decorators import login_required
from django.http import Http404



# Create your views here.
@login_required
def home(request):
    """home page for course log project"""
    courses = Course.objects.filter(owner=request.user)
    categories = Category.objects.filter(owner=request.user)
    entries = Entry.objects.filter(owner=request.user).order_by('-date')

    context = {'courses': courses, 'categories': categories, 'entries': entries}

    return render(request, 'course_logs/home.html', context)



@login_required
def all_courses(request):
    """ page showing all defined courses"""
    courses = Course.objects.filter(owner=request.user)
    context = {'courses': courses}
    
    return render(request, 'course_logs/all_courses.html', context)



@login_required
def all_categories(request):
    """ page showing all defined courses"""
    categories = Category.objects.filter(owner=request.user)
    context = {'categories': categories}
    
    return render(request, 'course_logs/all_categories.html', context)



@login_required
def this_course(request, course_id):
    course = Course.objects.get(id=course_id)
    if course.owner != request.user:
        raise Http404
    
    entries = course.entry_set.order_by('-date')
    context = {'course': course, 'entries': entries}

    return render(request, 'course_logs/this_course.html', context)



@login_required
def this_category(request, category_id):
    category = Category.objects.get(id=category_id)
    if category.owner != request.user:
        raise Http404
    entries = category.entry_set.order_by('-date')
    context = {'category': category, 'entries': entries}

    return render(request, 'course_logs/this_category.html', context)


@login_required
def this_entry(request, entry_id):
    entry = Entry.objects.get(id=entry_id)
    if entry.owner != request.user:
        raise Http404
    course = entry.course
    category = entry.category
    date = entry.date
    context = {'entry': entry, 'course': course, 'category':category, 'date': date}

    return render(request, 'course_logs/this_entry.html', context)




@login_required
def new_course(request):
    """Add a new course"""
    if request.method != 'POST': #i.e. request is probably GET=readonly
        # no data submitted. create a blank form
        form = CourseForm()
    else:
        # POST data submitted; process data
        form = CourseForm(data=request.POST)
        if form.is_valid():
            new_course = form.save(commit=False)
            new_course.owner = request.user
            new_course.save()
            return redirect('course_logs:all_courses')
        
        # display blank or invalid form
    context = {'form': form}
    return render(request, 'course_logs/new_course.html', context)



@login_required
def new_category(request):
    """Add a new category"""
    if request.method != 'POST': #i.e. request is probably GET=readonly
        # no data submitted. create a blank form
        form = CategoryForm()
    else:
        # POST data submitted; process data
        form = CategoryForm(data=request.POST)
        if form.is_valid():
            new_category = form.save(commit=False)
            new_category.owner = request.user
            new_category.save()
            return redirect('course_logs:all_categories')
        
        # display blank or invalid form
    context = {'form': form}
    return render(request, 'course_logs/new_category.html', context)



@login_required
def new_entry(request):
    if request.method != 'POST':
        # no data submitted. create a blank form
        form = EntryForm(user=request.user)
    else:
        # POST data submitted; process data
        form = EntryForm(data=request.POST, user=request.user)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.owner = request.user
            new_entry.save()
            return redirect('course_logs:home')
        
    context = {'form': form}
    return render(request, 'course_logs/new_entry.html', context)

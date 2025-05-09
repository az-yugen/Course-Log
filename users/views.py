from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def register(request):
    """Register a new user"""
    if request.method != 'POST':
        # display blank registration form
        form = UserCreationForm()
    else:
        # process completed form
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            # log the user in and then redirect to homepage
            login(request, new_user)
            return redirect('course_logs:home')
        
    # display blank or invalid form
    context = {'form': form}
    return render(request, 'registration/register.html', context)


def logoutUser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('registration/logged_out.html')
    return render(request, 'registration/logged_out.html')
    # return redirect('course_logs:home')

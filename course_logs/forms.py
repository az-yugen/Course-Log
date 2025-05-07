from django import forms
from .models import Course, Category, Entry

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['course']
        labels = {'course': ''}



class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['category']
        labels = {'category': ''}



class EntryForm(forms.ModelForm):

    def __init__(self,*args, user=None, **kwargs):
        super(EntryForm, self).__init__(*args, **kwargs)
        if user is not None:
            self.fields['course'].queryset = Course.objects.filter(owner=user)
            self.fields['category'].queryset = Category.objects.filter(owner=user)


    class Meta:
        model = Entry
        fields = ['date', 'course', 'category', 'description']
        widgets = {'date': forms.DateInput(
                    attrs={
                    'class': 'form-control',
                    'type': "date"
                    }
        )}

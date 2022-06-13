from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget

from django import forms

from courses.models import Course

class CourseForm(forms.Form):
    card_description = forms.CharField(widget=SummernoteInplaceWidget())

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        widgets = {
            'card_description': SummernoteInplaceWidget(),
        }

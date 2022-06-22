from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from django import forms

from courses.models import Course


class CourseForm(forms.Form):
    """
    form to include summernote as
    widget
    """
    card_description = forms.CharField(widget=SummernoteInplaceWidget())


class CourseForm(forms.ModelForm):
    """
    meta class for above
    """
    class Meta:
        model = Course
        widgets = {
            'card_description': SummernoteInplaceWidget(),
        }

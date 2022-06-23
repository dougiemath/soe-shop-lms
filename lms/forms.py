from django import forms
from django_summernote.widgets import SummernoteWidget

from .models import Lessons, LessonCategory
from courses.models import Course


class LessonForm(forms.ModelForm):
    """
    Form for adding a new lesson
    """
    class Meta:
        model = Lessons
        fields = '__all__'
        widgets = {
            'question_overview': SummernoteWidget(),
            'further_study': SummernoteWidget(),
            'question_approach': SummernoteWidget(),
            'sample_question_questions': SummernoteWidget(),
            'sample_question_text': SummernoteWidget(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = LessonCategory.objects.all()


class LessonCategoryForm(forms.ModelForm):
    """
    Form for adding a new category of lesson (such as 
    an exam name)
    """
    class Meta:
        model = LessonCategory
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class NewShopCourseForm(forms.ModelForm):
    """
    Form for adding a new shop content
    """
    class Meta:
        model = Course
        fields = '__all__'
        widgets = {
            'description': SummernoteWidget(),
            'card_description': SummernoteWidget(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

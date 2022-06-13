from django import forms

from .models import Lessons, LessonCategory
from courses.models import Course


class LessonForm(forms.ModelForm):

    class Meta:
        model = Lessons
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = LessonCategory.objects.all()


class LessonCategoryForm(forms.ModelForm):

    class Meta:
        model = LessonCategory
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class NewShopCourseForm(forms.ModelForm):

    class Meta:
        model = Course
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

from django.db import models

from ckeditor.fields import RichTextField

from lms.models import Lessons, LessonCategory

class Category(models.Model):

    class Meta:
        verbose_name_plural = "Categories"

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name

class Course(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=254)
    # card_description = models.TextField(null=True, blank=True)
    card_description = RichTextField(null=True, blank=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    course_length = models.IntegerField(null=True, blank=True)
    ##########
    course_category = models.ForeignKey(LessonCategory, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

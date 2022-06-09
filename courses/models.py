from django.db import models

from lms.models import CourseSkill

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
    card_description = models.TextField(null=True, blank=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    course_length = models.IntegerField(null=True, blank=True)
    courseskill = models.OneToOneField(CourseSkill, blank=True, null=True, on_delete=models.CASCADE, verbose_name="EXAM: (Leave blank if your course is General English)")

    def __str__(self):
        return self.name

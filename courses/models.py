from django.db import models

from lms.models import Lessons, LessonCategory


class Category(models.Model):
    """
    Class for creating course categories, such as
    exams and general English.
    """
    class Meta:
        verbose_name_plural = "Categories"

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Course(models.Model):
    """
    class for creating courses that will be
    on display in the shop side of the project
    """
    category = models.ForeignKey('Category', null=True,
                                 on_delete=models.SET_NULL,
                                 verbose_name="What is category"
                                 " of your lesson? It can be"
                                 "General English or Exam Skills.")
    name = models.CharField(max_length=254,
                            verbose_name="What is the name of your course?"
                            "THIS MUST BE THE SAME AS THE LESSON CATEGORY!")
    card_description = models.TextField(null=True,
                                        verbose_name="What is a brief "
                                        "description of your course?  "
                                        "This will appear in the shop's "
                                        "search results.")
    description = models.TextField(null=True,
                                   verbose_name="What is a "
                                   "detailed description of your course?  "
                                   "This will appear on the course's "
                                   "dedicated page, so be as detailed "
                                   "as you like.")
    price = models.DecimalField(max_digits=6, decimal_places=2)
    course_length = models.IntegerField(null=True,)
    course_category = models.ForeignKey(LessonCategory, null=True,
                                        on_delete=models.CASCADE,
                                        verbose_name="Now choose what"
                                        " lessons are included in this course."
                                        "  This step is very important!")
    course_meta = models.CharField(blank=True, verbose_name="This field "
                                   "is for SEO purposes.  Please enter some "
                                   "tags to describe your course and separate"
                                   " each tag with a comma.  For example, "
                                   "'IELTS, English, Exam'", max_length=50)

    def __str__(self):
        return self.name

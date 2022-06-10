
import uuid

from django.db import models
from django.urls import reverse

from embed_video.fields import EmbedVideoField

class CourseCategory(models.Model):
    
    class Meta:
        verbose_name_plural = "Course Categories"

    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class CourseSkill(models.Model):
    """defines the model for creating courses in the exams lms"""
    category = models.ForeignKey('CourseCategory', blank=True, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=True)
    SectionType = models.TextChoices('SectionType', 'Reading Writing Speaking Listening')
    exam_section = models.CharField(blank=True, choices=SectionType.choices, max_length=20)
    question_type = models.CharField(max_length=100)
    THUMBNAIL_IMAGES = [
        ('/reading.jpg', 'Reading'),
        ('/writing.jpg', 'Writing'),
        ('/listening.jpg', 'Listening'),
        ('/speaking.jpg', 'Speaking'),
    ]
    question_image = models.ImageField(choices=THUMBNAIL_IMAGES, default='Reading')
    question_overview = models.TextField(verbose_name = "Section 1 - Question Overview")
    sample_question_text = models.TextField(verbose_name = "Section 2 - Sample Passage (can be left blank)", blank=True)
    sample_question_questions = models.TextField(verbose_name = "Section 2 - Sample Questions")
    question_approach = models.TextField(verbose_name = "Section 3 - Question Approach")
    video = EmbedVideoField(blank=True, verbose_name = "Section 3 - Video")
    further_study = models.TextField(verbose_name = "Section 4 - Further Study Information")
    upload_questions = models.FileField(blank=True, verbose_name = "Section 4 - Further Practice Questions (PDF)")
    upload_answers = models.FileField(blank=True, verbose_name = "Section 4 - Further Practice Questions (Answers)")
    course_num = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("lms_content", args=[str(self.course_num)])

    class Meta:
        ordering = ['name']

    

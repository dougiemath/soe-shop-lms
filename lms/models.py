
import uuid

from django.db import models
from django.urls import reverse

from embed_video.fields import EmbedVideoField
from ckeditor.fields import RichTextField
from cloudinary.models import CloudinaryField

class LessonCategory(models.Model):
    
    class Meta:
        verbose_name_plural = "Lesson Categories"

    name = models.CharField(max_length=100, unique=True, verbose_name = "What is the name of the new category?")

    def __str__(self):
        return self.name

class Lessons(models.Model):
    """defines the model for creating courses in the exams lms"""
    category = models.ForeignKey('LessonCategory', blank=True, null=True, on_delete=models.CASCADE, verbose_name = "Choose a category for this lesson.  If it is a new category, not in the list, you will need to create a category in the previous section first:")
    name = models.CharField(max_length=100, null=True)
    SectionType = models.TextChoices('SectionType', 'Reading Writing Speaking Listening')
    exam_section = models.CharField(blank=True, choices=SectionType.choices, max_length=20, verbose_name = "If this lesson is for an exam, which section is it for?  Otherwise you can leave this blank.")
    THUMBNAIL_IMAGES = [
        ('reading.jpg', 'Reading'),
        ('writing.jpg', 'Writing'),
        ('listening.jpg', 'Listening'),
        ('speaking.jpg', 'Speaking'),
    ]
    question_image = CloudinaryField(choices=THUMBNAIL_IMAGES, default='Reading', verbose_name = "What skill does the lesson relate to?")
    question_type = models.CharField(max_length=100, verbose_name = "What kind of question is it?  Is it grammar, vocabulary or a specific exam question?")
    question_overview = RichTextField(verbose_name = "Section 1 - Question Overview")
    sample_question_text = RichTextField(verbose_name = "Section 2 - Sample Passage (can be left blank)", blank=True)
    sample_question_questions = RichTextField(verbose_name = "Section 2 - Sample Questions")
    question_approach = RichTextField(verbose_name = "Section 3 - Question Approach")
    video = EmbedVideoField(blank=True, verbose_name = "Section 3 - Video")
    further_study = RichTextField(verbose_name = "Section 4 - Further Study Information")
    upload_questions = models.FileField(blank=True, verbose_name = "Section 4 - Further Practice Questions (PDF)")
    upload_answers = models.FileField(blank=True, verbose_name = "Section 4 - Further Practice Questions (Answers)")
    course_num = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("lms_content", args=[str(self.course_num)])

    class Meta:
        ordering = ['name']
        verbose_name_plural = "Lessons"

    

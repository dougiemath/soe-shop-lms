from django.db import models
from  embed_video.fields  import  EmbedVideoField


# Create your models here.

class ExamCategory(models.Model):
    
    class Meta:
        verbose_name_plural = "Exam Categories"
        
    exam_name = [
        ('KET', 'KET'),
        ('PET', 'PET'),
        ('FCE', 'FEC'),
        ('CAE', 'CAE'),
        ('CPE', 'CPE'),
        ('IELTS', 'IELTS'),
    ]
    name = models.CharField(choices=exam_name, max_length=50)

    def __str__(self):
        return self.name

class ExamSkill(models.Model):
    """defines the model for creating courses in the exams lms"""
    exam_names = [
        ('KET', 'KET'),
        ('PET', 'PET'),
        ('FCE', 'FEC'),
        ('CAE', 'CAE'),
        ('CPE', 'CPE'),
        ('IELTS', 'IELTS'),
    ]
    exam_name = models.CharField(choices=exam_names, max_length=50)
    SectionType = models.TextChoices('SectionType', 'Reading writing Speaking Listening')
    exam_section = models.CharField(blank=True, choices=SectionType.choices, max_length=20)
    question_type = models.CharField(max_length=100)
    THUMBNAIL_IMAGES = [
    ('/reading.jpg', 'Reading'),
    ('/writing.jpg', 'Writing'),
    ('/listening.jpg', 'Listening'),
    ('/speaking.jpg', 'Speaking'),
    ]
    question_image = models.ImageField(choices=THUMBNAIL_IMAGES, default='Reading')
    question_overview = models.TextField()
    sample_question_text = models.TextField()
    sample_question_questions = models.TextField()
    question_approach = models.TextField()
    video = EmbedVideoField(blank=True)
    upload_questions = models.FileField(blank=True)
    upload_answers = models.FileField(blank=True)


    def __str__(self):
        return self.exam_name

    class Meta:
        ordering = ['exam_name']

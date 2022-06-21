from django.db import models


class Contact(models.Model):
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    BOOL_CHOICES = ((True, 'Yes'), (False, 'No'))
    newsletter = models.BooleanField(null=True, choices=BOOL_CHOICES, default=True, verbose_name="Would you like to sign up for our newsletter?")

    def __str__(self):
        return self.email
    
    class Meta:
        ordering = ["-date"]

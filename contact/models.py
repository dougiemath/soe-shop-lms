from django.db import models


class Contact(models.Model):
    """
    Model for creating contact form
    """
    email = models.EmailField(blank=False)
    subject = models.CharField(max_length=255)
    message = models.TextField(blank=False)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

    class Meta:
        ordering = ["-date"]

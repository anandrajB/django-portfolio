from django.db import models

# Create your models here.
class contact(models.Model):
    email = models.CharField(max_length=50)
    subject = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.email


#for resume upload

class files(models.Model):
    resume = models.FileField(upload_to='assets/media')
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title
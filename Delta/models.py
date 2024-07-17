from django.db import models

class Delta(models.Model):
    title = models.CharField(max_length=100)
    picture = models.ImageField(upload_to='photos/')
    detail = models.CharField(max_length=100)
    idea = models.CharField(max_length=100)
    studyTime = models.CharField(max_length=100)
    profile = models.CharField(max_length=100)

class Article(models.Model):
    title = models.FileField()


class UploadedFile(models.Model):
    file = models.FileField()
    uploaded_on = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.uploaded_on.date()
from django.db import models

class Delta(models.Model):
    title = models.CharField(max_length=100, default='default_value')
    picture = models.ImageField(upload_to='photos/', default='default_value')
    detail = models.CharField(max_length=100, default='default_value')
    idea = models.CharField(max_length=100, default='default_value')
    studyTime = models.CharField(max_length=100, default='default_value')
    profile = models.CharField(max_length=100, default='default_value')

class Article(models.Model):
    title = models.FileField()


class UploadedFile(models.Model):
    file = models.FileField()
    uploaded_on = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.uploaded_on.date()
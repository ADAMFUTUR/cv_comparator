from django.db import models

# Create your models here.

class CV(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    skills = models.TextField()
    experience = models.IntegerField()
    education = models.TextField()
    file = models.FileField(upload_to='cvs/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class JobRequirement(models.Model):
    title = models.CharField(max_length=100)
    required_skills = models.TextField()
    
    def __str__(self):
        return self.title

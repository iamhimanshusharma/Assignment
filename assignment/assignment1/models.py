from django.db import models

# Create your models here.
class Grade(models.Model):
    GradeID = models.CharField(max_length=100, null=False)
    Grade = models.CharField(max_length=200, null=False)

class Subject(models.Model):
    SubjectID = models.CharField(max_length=100, null=False)
    Subject = models.CharField(max_length=500, null=False)

class Question(models.Model):
    QuestionsText = models.CharField(max_length=100, null=True)
    GradeId = models.CharField(max_length=100, null=False)
    Grade = models.CharField(max_length=200, null=True)
    SubjectID = models.CharField(max_length=100, null=False)
    Subject = models.CharField(max_length=500, null=True)



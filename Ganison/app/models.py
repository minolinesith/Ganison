from django.db import models

# Create your models here.

class School(models.Model):
    school_name = models.CharField(max_length=200)

class Class(models.Model):
    Class = models.CharField(max_length=200)

class Assesment_Areas(models.Model):
    assesment_areas = models.CharField(max_length=200)

class Student(models.Model):
    StudentID = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)

class Answers(models.Model):
    Answers = models.CharField(max_length=200)

class Summary(models.Model):
    sydney_participants=models.CharField(max_length=200)
    sydney_percentile = models.CharField(max_length=200)
    correct_answer_percentage_per_class = models.CharField(max_length=200)
    participant = models.CharField(max_length=200)
    correct_answers = models.CharField(max_length=200)
    year_level = models.CharField(max_length=200)
    average_score = models.CharField(max_length=200)

class Awards(models.Model):
    award = models.CharField(max_length=200)

class Subject(models.Model):
    Subject = models.CharField(max_length=200)







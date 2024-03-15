from django.db import models

class DataType(models.Model):
    name = models.CharField(max_length=100, null=True)
    birthdate = models.CharField(max_length=100, null=True)
    score = models.CharField(max_length=100, null=True)
    grade = models.CharField(max_length=100, null=True)
    row_number = models.CharField(max_length=100, null=True)
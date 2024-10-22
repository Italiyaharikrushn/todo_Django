from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=250)
    desc = models.CharField(max_length=500)
    status = models.CharField(max_length=20)
    completion_date = models.DateTimeField(null=True,blank=True)

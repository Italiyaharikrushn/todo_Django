from django.db import models

class Todo(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField(null=True, blank=True)
    is_complete = models.BooleanField(default=False)
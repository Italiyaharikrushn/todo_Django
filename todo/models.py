# from django.db import models

# class Todo(models.Model):
#     name = models.CharField(max_length=100)
#     description = models.TextField()
#     date = models.DateField(null=True, blank=True)
#     is_complete = models.CharField(max_length=20)



from django.db import models

class Todo(models.Model):
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=500)
    is_complete = models.CharField(max_length=20)
    date = models.DateTimeField(null=True,blank=True)
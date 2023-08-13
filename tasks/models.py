from django.db import models

# Create your models here.

class TaskStoreModel(models.Model):

    id = models.AutoField(primary_key=True)
    taskTitle = models.CharField(max_length=20)
    taskDescription = models.CharField(max_length=150)
    isCompleted = models.BooleanField(default=False)

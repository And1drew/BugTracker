from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import datetime


# Create your models here.
class custom_user(AbstractUser):
    def __str__(self):
        return self.username


class bug_ticket(models.Model):
    title = models.CharField(max_length = 80)
    description = models.TextField()
    status_choices = [
        ('New', 'New'),
        ('In Progress', 'In Progress'),
        ('Done', 'Done'),
        ('Invalid', 'Invalid'),
    ]
    status = models.CharField(choices = status_choices, default='New', max_length=11)
    created_by = models.ForeignKey(custom_user, on_delete=models.DO_NOTHING)
    date = models.DateTimeField(default = datetime.now)
    assigned = models.CharField(default = None, blank = False, null = True, max_length = 30)
    completed_by = models.CharField(default = None, blank = False, null = True, max_length = 30)
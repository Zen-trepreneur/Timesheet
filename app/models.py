from django.db import models
from django.contrib.auth.models import User


class TimeEntryModel(models.Model):
    PROJECT_LIST = [
        ('project1', 'Project --- (1)'),
        ('project2', 'Project --- (2)'),
        ('project3', 'Project --- (3)'),
        ('project4', 'Project --- (4)'),
        ('project5', 'Project --- (5)'),
        ('project6', 'Project --- (6)')
    ]

    dev = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.CharField(max_length=100)
    project = models.CharField(max_length=100, choices=PROJECT_LIST)
    datetime_start = models.DateTimeField()
    datetime_end = models.DateTimeField()

    def __str__(self):
        return f"{self.dev} --is associated with Project : {self.project}"

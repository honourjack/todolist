# zeze/models.py

from django.contrib.auth.models import User as DjangoUser
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(DjangoUser, on_delete=models.CASCADE)
    # You can add more fields to the profile if needed

    def __str__(self):
        return self.user.username

class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    due_date = models.DateField()
    status = models.BooleanField(default=False)  # False for not completed, True for completed
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title

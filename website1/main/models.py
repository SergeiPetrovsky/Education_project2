from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    fio = models.CharField(max_length=100, default="")
    job = models.CharField(max_length=50, default="")
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    # def __str__(self):
    #     return self.title

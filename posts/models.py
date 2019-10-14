from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from json import loads, dumps
from django.urls import reverse

# Create your models here.
class Question(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    title = models.CharField(max_length = 100)
    description = models.TextField()
    date = models.DateField(default = timezone.now)
    tags = models.CharField(max_length= 90)

    def set_tags(self, tags):
        self.tags = dumps(tags)
        return self.tags
    
    def get_tags(self):
        return self.tags

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})


class Answer(models.Model):
    user = models.CharField(max_length= 150)
    
    question = models.ForeignKey(
        Question, on_delete = models.CASCADE, 
        related_name = 'answer', default = 2)

    description = models.TextField()
    date = models.DateField(default = timezone.now)

    def __str__():
        return self.description
    

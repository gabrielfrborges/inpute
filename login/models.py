from django.db import models
from django.contrib.auth.models import User, Group
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    user_ra = models.CharField(max_length= 30)
    USER_COURSES_CHOICES = (
      (1, 'student'),
      (2, 'teacher'),
      (3, 'secretary'),
      (4, 'supervisor'),
      (5, 'admin'),
    )

    user_course = models.PositiveSmallIntegerField(choices=USER_COURSES_CHOICES)
    


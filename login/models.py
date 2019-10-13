from django.db import models
from django.contrib.auth.models import User, Group
from django.db.models.signals import post_save
from django.core.exceptions import ObjectDoesNotExist
from django.dispatch import receiver


# Create your models here.
class Profile(models.Model):
  user = models.OneToOneField(User, on_delete = models.CASCADE)
  user_ra = models.CharField(max_length= 30)
  COURSE_CHOISES= [
    ('BD', 'Banco de dados'),
    ('ADS','Analise e desenvolvimento de sistemas')
  ]
  user_course = models.CharField(max_length= 5, choices= COURSE_CHOISES, default= 'ADS')
  
  @property
  def full_name(self):
    return  '{} {}'.format(self.first_name, self.last_name)

  def __str__(self):
    return self.user.username

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
  if created:
    Profile.objects.create(user=instance)
  try:
    instance.profile.save()
  except ObjectDoesNotExist:
    Profile.objects.create(user=instance)
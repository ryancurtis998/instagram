from django.db import models
from django.db import models
from django.contrib.auth.models import User
import datetime as dt
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.
#models for location
class Location(models.Model):
    location_det = models.CharField(max_length=30)

    def __str__(self):
        return self.location_det

#models for inages
class Image(models.Model):
    # username = models.OneToOneField(User, on_delete=models.CASCADE,)
    # image_location = models.ForeignKey(Location)
    image_path = models.ImageField(upload_to = 'gallery/')
    image_description = models.CharField(max_length=100, blank=True)


    def __str__(self):
        return self.image_description
class Comments(models.Model):
    comment=models.CharField(max_length=100)
    user_id=models.ForeignKey(User,blank=True, on_delete=models.CASCADE,related_name='user',null=True)
    image_id=models.ForeignKey(Image,blank=True, on_delete=models.CASCADE,related_name='image_comments',null=True)
    date_posted=models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural= 'Comments'

    def __str__(self):
        return self.comment

class Profile(models.Model):
    profile_photo = models.ImageField(upload_to = 'profiles/')
    first_name=models.CharField(max_length=30, blank=True)
    last_name=models.CharField(max_length=30, blank=True)
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    website=models.CharField(max_length=50, blank=True)
    bio = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.first_name

    def save_user(self):
        self.save()

    @receiver(post_save,sender=User)
    def create_user_profile(sender,instance,created,**kwargs):
        if created:
            Profile.objects.create(user_id=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    photo = models.FileField(upload_to='images/', null=True, blank=True, help_text="Upload only .png, .jpg & .jpeg image extension.")
    contact = models.IntegerField()

    def __str__(self):
        return self.user.username

    class Meta:
        db_table = 'profile'
        verbose_name_plural = 'PROFILE'
        managed = True
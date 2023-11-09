# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    bio = models.CharField(max_length=255, null=True, blank=True)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Gsm_User(models.Model):

    #__Gsm_User_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    photo_path = models.CharField(max_length=255, null=True, blank=True)
    password = models.CharField(max_length=255, null=True, blank=True)

    #__Gsm_User_FIELDS__END

    class Meta:
        verbose_name        = _("Gsm_User")
        verbose_name_plural = _("Gsm_User")


class Like(models.Model):

    #__Like_FIELDS__

    #__Like_FIELDS__END

    class Meta:
        verbose_name        = _("Like")
        verbose_name_plural = _("Like")


class Photo(models.Model):

    #__Photo_FIELDS__
    path = models.CharField(max_length=255, null=True, blank=True)

    #__Photo_FIELDS__END

    class Meta:
        verbose_name        = _("Photo")
        verbose_name_plural = _("Photo")


class Couple(models.Model):

    #__Couple_FIELDS__

    #__Couple_FIELDS__END

    class Meta:
        verbose_name        = _("Couple")
        verbose_name_plural = _("Couple")



#__MODELS__END

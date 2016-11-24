from __future__ import unicode_literals

from django.db import models

class User(models.Model):
    created = models.DateTimeField(auto_now_add=True, blank=True)
    username = models.CharField(max_length=30, blank=True)
    email = models.EmailField(blank=True)
    fname = models.CharField(max_length=30, blank=True)
    lname = models.CharField(max_length=30, blank=True)
    profile_url = models.ImageField(upload_to=None, height_field=None, width_field=None, blank=True)

    class Meta:
        ordering = ('created',)

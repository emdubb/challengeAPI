from __future__ import unicode_literals

from django.db import models

class User(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    username = models.CharField(max_length=30)
    email = models.EmailField()
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    profile_url = models.ImageField(upload_to=None, height_field=None, width_field=None)

    class Meta:
        ordering = ('created',)

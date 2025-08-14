from django.db import models
from django.contrib.auth.models import AbstractUser


class User(models.Model):
    u_id = models.BigAutoField(primary_key=True)
    u_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, blank=True, null=True)
    password = models.CharField(max_length=255)
    token = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'user'  # use your existing table name



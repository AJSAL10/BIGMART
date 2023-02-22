from django.db import models

# Create your models here.


class weblogindb(models.Model):
    UNAME = models.CharField(max_length=100, null=True, blank=True)
    EMAIL = models.EmailField(null=True, blank=True)
    PASSWORD = models.CharField(max_length=50, null=True, blank=True)
    CFMPASSWORD = models.CharField(max_length=50, null=True, blank=True)
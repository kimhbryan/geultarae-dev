from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from datetime import timedelta


class User(AbstractUser):
    pass


class Writing(models.Model):
    title = models.CharField(max_length=200)
    hint = models.CharField(max_length=200, help_text="힌트")
    date_available = models.DateTimeField()
    text = models.TextField(max_length=10000, null=True)

    @property
    def is_available(self):
        return bool(self.date_available <= timezone.now() < self.date_available + timedelta(days=1))

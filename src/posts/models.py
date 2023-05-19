from django.db import models

from users.models import User


class Post(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    content = models.CharField(max_length=10000)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    published_date = models.DateTimeField()


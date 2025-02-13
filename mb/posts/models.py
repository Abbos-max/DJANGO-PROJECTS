from django.db import models
from django.contrib.auth.models import User
user = User.objects.filter(is_superuser=True).first()
print(user.username, user.email)

class Post(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text[:50]








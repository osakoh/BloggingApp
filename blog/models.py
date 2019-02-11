from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=130)
    content = models.TextField()
    # shows the current time
    date_posted = models.DateTimeField(default=timezone.now)
    # Tells django to delete a post if a user has been deleted
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
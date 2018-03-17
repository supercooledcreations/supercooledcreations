# Import
# Django
from django.contrib.auth import get_user_model
from django.db import models


# Models
class Bookmark(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    name = models.CharField(max_length=140)
    url = models.URLField()

    def __str__(self):
        return self.name

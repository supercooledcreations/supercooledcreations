# Import
from django.contrib.auth import get_user_model
from django.db import models


# Models
class Task(models.Model):

    STATUS_CHOICES = (
        ('outerspace', 'Launch It!'),
        ('headspace', 'In Headspace'),
        ('desk', 'On Desk'),
        ('monitor', 'Monitor'),
        ('board', 'On the Board'),
        ('icebox', 'In the Icebox'),
        ('bin', 'Throw it in the Bin'),
    )

    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    parent_task = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=128)
    status = models.CharField(max_length=32, choices=STATUS_CHOICES)

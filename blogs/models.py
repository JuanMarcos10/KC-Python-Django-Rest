from django.contrib.auth.models import User
from django.db import models


class Blog(models.Model):

    IMPORTANT = 'IMP'
    INFORMATION = 'INF'
    NOTE = 'NOT'

    LICENSES = [
        [IMPORTANT, 'Important'],
        [INFORMATION, 'Information'],
        [NOTE, 'Note']
    ]

    PUBLIC = 'PUB'
    PRIVATE = 'PRI'

    VISIBILITY = [
        [PUBLIC, 'Public'],
        [PRIVATE, 'Private']
    ]

    title = models.CharField(max_length=150)
    text = models.CharField(max_length=150)
    description = models.TextField(null=True, blank=True)
    url = models.URLField()
    creation_date = models.DateTimeField(auto_now_add=True)
    modification_date = models.DateTimeField(auto_now=True)
    category = models.CharField(max_length=3, choices=LICENSES, default=INFORMATION)
    owner = models.ForeignKey(User, related_name='blogs', on_delete=models.CASCADE)
    visibility = models.CharField(max_length=3, choices=VISIBILITY, default=PUBLIC)

    def __str__(self):
        return self.title

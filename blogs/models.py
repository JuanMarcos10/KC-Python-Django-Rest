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

    title = models.CharField(max_length=150)
    text = models.CharField(max_length=150)
    description = models.TextField(null=True, blank=True)
    url = models.URLField()
    creation_date = models.DateTimeField(auto_now_add=True)
    modification_date = models.DateTimeField(auto_now=True)
    category = models.CharField(max_length=3, choices=LICENSES, default=INFORMATION)

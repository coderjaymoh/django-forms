from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=100, default='', blank=True)
    main = models.IntegerField(default='', blank=True)

    def __str__(self):
        return self.title

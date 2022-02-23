from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=255)
    descriptions = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.title} >>> {self.descriptions}'



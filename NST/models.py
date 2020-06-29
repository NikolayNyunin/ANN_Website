from django.db import models


class Style(models.Model):
    name = models.CharField(max_length=40)
    image = models.ImageField(upload_to='styles/')

    def __str__(self):
        return self.name

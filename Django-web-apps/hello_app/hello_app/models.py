from django.db import models

class PersonModel(models.Model):
    title = models.CharField(max_length = 100)
    description = models.TextField()

    def __str__(Self):
        return self.title







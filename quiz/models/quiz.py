from django.db import models


class Quiz(models.Model):
    name = models.CharField(max_length=200)
    start_date = models.DateTimeField('Start date')
    end_date = models.DateTimeField('End date')
    description = models.TextField()

    def __str__(self):
        return self.name

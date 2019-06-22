from django.db import models

class StartDate(models.Model):
    start_date = models.DateField('start date')

    def __str__(self):
        return self.start_date


class EndDate(models.Model):
    end_date = models.DateField('end date')

    def __str__(self):
        return self.end_date
import datetime

from django.db import models
from django.utils import timezone

class Eggs(models.Model):
    customer = models.CharField(max_length=200)
    quantity = models.FloatField(default=0)
    price = models.FloatField(default=0)
    type = models.CharField(max_length=6)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.customer

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

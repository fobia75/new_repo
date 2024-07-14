from django.db import models
from django.utils  import timezone

class Coin(models.Model):
    time = models.DateTimeField(default = timezone.now)
    site = models.CharField(max_length= 10)


    @staticmethod
    def value_coin():
        value_ = Coin.objects.order_by('-time')[:5]
        return value_


    def __str__(self):
        return f'time: {self.time}, site: {self.site}' 

from django.db import models
from django.conf import settings

# Create your models here.
class AdventureRecords(models.Model):
    devilzone = models.IntegerField(default=0)
    village = models.IntegerField(default=0)
    cave = models.IntegerField(default=0)
    capitalroad = models.IntegerField(default=0)
    desert = models.IntegerField(default=0)
    palace = models.IntegerField(default=0)
    mazetower = models.IntegerField(default=0)
    storybook = models.IntegerField(default=0)
    bossroom = models.IntegerField(default=0)
    blacktower = models.IntegerField(default=0)
    holder = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return f"{self.blacktower}{self.bossroom}{self.storybook}{self.mazetower}{self.palace}{self.desert}{self.capitalroad}{self.cave}{self.village}{self.devilzone}"
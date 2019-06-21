from django.db import models

# Create your models here.
class AdventureRecords(models.Model):
    devilzone = models.IntegerField()
    village = models.IntegerField()
    cave = models.IntegerField()
    capitalroad = models.IntegerField()
    desert = models.IntegerField()
    palace = models.IntegerField()
    mazetower = models.IntegerField()
    storybook = models.IntegerField()
    bossroom = models.IntegerField()
    blacktower = models.IntegerField()

    def __str__(self):
        return f"{self.blacktower}{self.bossroom}{self.storybook}{self.mazetower}{self.palace}{self.desert}{self.capitalroad}{self.cave}{self.village}{self.devilzone}"
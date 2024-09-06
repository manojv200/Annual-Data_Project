from django.db import models


# Create your models here.
class QuarterlyProduction(models.Model):
    api_well_number = models.IntegerField()
    quarter = models.IntegerField()
    oil = models.IntegerField()
    gas = models.IntegerField()
    brine = models.IntegerField()


class AnnualProduction(models.Model):
    api_well_number = models.IntegerField(unique=True)
    total_oil = models.IntegerField()
    total_gas = models.IntegerField()
    total_brine = models.IntegerField()

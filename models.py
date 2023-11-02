from django.db import models
from django_countries.fields import CountryField
from picklefield.fields import PickledObjectField

# Create your models here.
class Directory(models.Model):

    PERIODIC = {
        ('Daily', 'Daily'),
        ('Weekly', 'Weekly'),
        ('Monthly', 'Monthly'),
        ('Quarterly', 'Quarterly'),
        ('Annually', 'Annually')
    }

    DESCRIPTION = {
        ('National Accounts', 'A'),
        ('Production, Shipment, Inventories & Orders', 'B'),
        ('Land, Construction & Properties', 'C'),
        ('Government Revenues & Expenditures', 'D'),
        ('Domestic & Foreign Debts', 'E'),
        ('Demography & Labour Market', 'F'),
        ('Wholesale & Retail Trades', 'G'),
        ('Inflation', 'H'),
        ('Balance of Payments', 'I'),
        ('Foreign Trade & Investment', 'J'),
        ('Money & Banking', 'K'),
        ('Interest & Foreign Exchange Rates', 'L'),
        ('Household Incomes & Expenditures', 'M'),
        ('Business & Corporation Activities', 'N'),
        ('Energy', 'O'),
        ('Automobiles', 'P'),
        ('Tourism', 'Q'),
        ('Economic & Business Surveys', 'R'),
        ('Transportation & Communication', 'S'),
        ('Daily Statistics', 'Y'),
        ('Financial Markets', 'Z')
    }

    id = models.IntegerField(primary_key=True)
    link = models.URLField()
    country = CountryField(blank=True)
    periodic = models.CharField(max_length=100, choices=PERIODIC)
    topics = models.CharField(max_length=1000, choices=DESCRIPTION)
    last_update = models.CharField(max_length=100, blank=True) 
    next_release = models.CharField(max_length=100, blank=True) 
    comments = models.TextField(blank=True)
    getfile = models.FileField(blank=True, null=True)
    filepresent = models.CharField(max_length=100, blank=True)
    eachtable = PickledObjectField(blank=True, null=True)
    def __str__(self):
        return self.country

# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from datetime import datetime, timedelta

# Create your models here.
class MeterReadings(object) :
    '''
    factory to MeterReading
    '''
    def new(self, date, reading) :
        return MeterReading.objects.create(date = date, reading = reading).pk

    def get(self, pk) :
        return MeterReading.objects.filter(pk = pk).first()

    def delete(self, pk) :
        pass

class MeterReading(models.Model) :
    '''
    model class for the meter reading
    '''
    date = models.DateField(verbose_name = 'Date of reading')
    reading = models.FloatField(verbose_name = 'Meter reading')

    def date_is_in_the_future(self) :
        # this formats the variable to YYYY-MM-DD
        date_tomorrow = str(datetime.today() + timedelta(days = 1))[:10]
        date_today = str(self.date)
        if str(self.date) < date_tomorrow :
            return False
        return True

    def save(self, *args, **kwargs) :
        if(self.date_is_in_the_future()) :
            return

        super(MeterReading, self).save(*args, **kwargs)

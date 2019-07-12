# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from datetime import datetime, timedelta
from .utilities import Utilities
from math import isnan

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
    reading = models.FloatField(verbose_name = 'Meter reading', blank = True)

    def save(self, *args, **kwargs) :
        if(Utilities.date_is_in_the_future(self.date)) :
            return
        if(self.reading is None) :
            return
        if(isnan(self.reading)) :
            return
        if(self.reading < 0) :
            return

        super(MeterReading, self).save(*args, **kwargs)

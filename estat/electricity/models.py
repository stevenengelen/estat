# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class MeterReadings(object) :
    '''
    factory to MeterReading
    '''
    def new(self, date, reading) :
        meter_reading = MeterReading()
        meter_reading.date = date
        meter_reading.reading = reading
        meter_reading.save()
        return meter_reading.pk

    def get(self, pk) :
        MeterReading.objects.filter(pk = pk)
        pass

    def delete(self, pk) :
        pass

class MeterReading(models.Model) :
    '''
    model class for the meter reading
    '''
    date = models.DateField(verbose_name = 'Date of reading')
    reading = models.FloatField(verbose_name = 'Meter readng')

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import HttpResponseRedirect
from electricity.forms import RegisterMeterReadingForm
from electricity.models import MeterReading

# Create your views here.
class TaskRegisterMeterReading(View) :
    def get(self, request) :
        form = RegisterMeterReadingForm()
        meter_readings = MeterReading.objects.all()
        if meter_readings :
            print(meter_readings.first().date)
        return render(request, 'home.html', { 'registerMeterReadingForm' : form, 'meterReadings' : meter_readings })

    def post(self, request) :
        # form = RegisterMeterReadingForm()
        # if request.method == 'POST' :
        meter_readings = MeterReading.objects.all()
        form = RegisterMeterReadingForm(request.POST)
        if form.is_valid() :
            form.save()
            return render(request, 'home.html', { 'registerMeterReadingForm' : RegisterMeterReadingForm(), 'meterReadings' : meter_readings })
        return render(request, 'home.html', { 'registerMeterReadingForm' : form, 'meterReadings' : meter_readings })

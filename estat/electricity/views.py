# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import HttpResponseRedirect
from electricity.forms import RegisterMeterReadingForm
from electricity.models import MeterReading
import pdb

# Create your views here.
class TaskRegisterMeterReading(View) :
    def get(self, request) :
        form = RegisterMeterReadingForm()
        meter_readings = MeterReading.objects.all()
        return render(request, 'home.html', { 'registerMeterReadingForm' : form, 'meterReadings' : meter_readings })

    def post(self, request) :
        # pdb.set_trace()
        form = RegisterMeterReadingForm(request.POST)
        meter_readings = MeterReading.objects.all()
        if form.is_valid() :
            form.save()
            # TODO can we do a redirect to home here?
            return render(request, 'home.html', { 'registerMeterReadingForm' : RegisterMeterReadingForm(), 'meterReadings' : meter_readings })
        # TODO can we do a redirect to home here? No we can not, because we need the form data
        return render(request, 'home.html', { 'registerMeterReadingForm' : form, 'meterReadings' : meter_readings })

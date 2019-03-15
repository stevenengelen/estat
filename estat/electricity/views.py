# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponseRedirect

# Create your views here.
class Home(View) :
    def get(self, request) :
        # print('in Home.get')
        return render(request, 'home.html')

    def post(self, request) :
        # print('in Home.post')
        return HttpResponseRedirect('/')

def post_reading(request) :
    print('in post_reading')

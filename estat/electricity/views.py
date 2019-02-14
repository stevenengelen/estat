# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import View

# Create your views here.
class Home(View) :
    def get(self, request) :
        return render(request, 'home.html')

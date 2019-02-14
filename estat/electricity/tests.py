# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

# Create your tests here.

class HomePageTest(TestCase) :
    def test_estat_page_is_online(self) :
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

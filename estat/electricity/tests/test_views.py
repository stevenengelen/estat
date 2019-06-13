from django.test import TestCase
from unittest import skip
from django.utils.html import escape
from electricity.models import MeterReading
from electricity.tests.test_models import DATE, READING, TOMORROW
from electricity.forms import RegisterMeterReadingForm
from datetime import datetime
from datetime import timedelta

class HomepageTests(TestCase) :
    template_name = 'home.html'

    def test_uses_homepage_template(self) :
        response = self.client.get('/')
        self.assertTemplateUsed(response, self.template_name)

    def test_homepage_shows_meter_reading_form(self) :
        response = self.client.get('/')
        # print(response.content.decode())
        self.assertIsInstance(response.context['registerMeterReadingForm'], RegisterMeterReadingForm, msg = 'homepage does not contain an instance of RegisterMeterReadingForm')
        self.assertContains(response, 'id_date')
        self.assertContains(response, 'id_reading')
        self.assertContains(response, 'id_submit')

    def test_homepage_contains_table_with_meter_readings(self) :
        response = self.client.get('/')
        self.assertContains(response, 'id_table_readings')

    @skip
    def test_POST_valid_reading_and_date_redirects_to_home_page(self) :
        response = self.client.post('/reading', data = { 'date' : DATE, 'reading' : READING } )
        iself.assertRedirects(response, '/')

    def test_POST_valid_reading_and_date_is_stored(self) :
        response = self.client.post('/reading', data = { 'date' : DATE, 'reading' : READING })
        meter_readings = MeterReading.objects.all()
        self.assertEqual(len(meter_readings), 1, msg = 'valid post request is not stored')
        meter_reading = meter_readings.first()
        self.assertEqual(str(meter_reading.date), DATE, msg = 'valid post request did not store date correctly')
        self.assertEqual(meter_reading.reading, READING, msg = 'valid post request did not store reading correctly')

    def test_POST_valid_reading_and_date_is_shown_in_table_on_homepage(self) :
        response = self.client.post('/reading', data = { 'date' : DATE, 'reading' : READING })
        self.assertContains(response, DATE)
        self.assertContains(response, READING)

    @skip
    def test_POST_invalid_redirects_to_home_page(self) :
        response = self.client.post('/reading', data = { 'date' : DATE, 'reading' : -READING } )
        self.assertRedirects(response, '/')

    def test_POST_negative_reading_displays_error_message(self) :
        response = self.client.post('/reading', data = { 'date' : DATE, 'reading' : -READING } )
        self.assertContains(response, escape('The meter is not capable to display a negative electricity consumation, so a negative reading is not possible'))

    def test_POST_invalid_date_in_the_future_displays_error_message(self) :
        response = self.client.post('/reading', data = { 'date' : TOMORROW, 'reading' : READING } )
        self.assertContains(response, escape('You can not submit a reading made in the future'))

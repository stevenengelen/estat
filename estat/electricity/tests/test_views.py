from django.test import TestCase
from unittest import skip
from django.utils.html import escape
from electricity.models import MeterReading
from electricity.tests.test_models import DATE, READING
from electricity.forms import RegisterMeterReadingForm

class HomepageTests(TestCase) :
    template_name = 'home.html'

    '''----------------------------------------
    |     Use Case Register meter Reading     |
    ----------------------------------------'''
    '''
    happy path
    '''
    def test_uses_homepage_template(self) :
        response = self.client.get('/')
        self.assertTemplateUsed(response, self.template_name)

    def test_homepage_shows_meter_reading_form(self) :
        response = self.client.get('/')
        self.assertIsInstance(response.context['registerMeterReadingForm'], RegisterMeterReadingForm, msg = 'homepage does not contain an instance of RegisterMeterReadingForm')

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

    def test_homepage_contains_table_with_meter_readings(self) :
        response = self.client.get('/')
        self.assertContains(response, 'id_table_readings')

    def test_POST_valid_reading_and_date_is_shown_in_table_on_homepage(self) :
        response = self.client.post('/reading', data = { 'date' : DATE, 'reading' : READING })
        print('-----------------------')
        print(response.content.decode())
        print(MeterReading.objects.all().first().date)
        print(MeterReading.objects.all().first().reading)
        self.assertContains(response, DATE)# , status_code = 302)
        self.assertContains(response, READING)#, status_code = 302)

    @skip
    def test_POST_invalid_redirects_to_home_page(self) :
        response = self.client.post('/reading', data = { 'date' : DATE, 'reading' : '-15' } )
        self.assertRedirects(response, '/')

    @skip
    def test_POST_negative_reading_displays_error_message(self) :
        response = self.client.post('/reading', data = { 'date' : DATE, 'reading' : '-15' } )
        self.assertContains(response, escape('The meter is not capable to display a negative electricity consumation, so a negative reading is not possible.'), status_code = 302)

    @skip
    def test_POST_invalid_reading_displays_error_message(self) :
        pass

    @skip
    def test_POST_invalid_date_displays_error_message(self) :
        pass

    @skip
    def test_home_page_contains_correct_html(self) :
        pass

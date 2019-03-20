from django.test import TestCase
from unittest import skip
from django.utils.html import escape

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

    def test_POST_valid_reading_and_date_redirects_to_home_page(self) :
        response = self.client.post('/reading', data = { 'date' : '2019-03-12', 'reading' : '15' } )
        self.assertRedirects(response, '/')

    def test_POST_valid_reading_and_date_is_stored(self) :
        self.client.post('/reading', data = { 'date' : '2019-03-12', 'reading' : '15' } )
        self.assertEqual(MeterReadings.objects.all(), 1, 'valid post request is not stored')
        date = MeterReadings.objects.first().date
        self.assertEqual(date, '2019-03-12', 'date is not correctly stored')
        reading = MeterReadings.objects.first().reading
        self.assertEqual(reading, '15', 'reading is not correctly stored')

    @skip
    def test_POST_invalid_redirects_to_home_page(self) :
        response = self.client.post('/reading', data = { 'date' : '2019-03-12', 'reading' : '-15' } )
        self.assertRedirects(response, '/')

    @skip
    def test_POST_negative_reading_displays_error_message(self) :
        response = self.client.post('/reading', data = { 'date' : '2019-03-12', 'reading' : '-15' } )
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

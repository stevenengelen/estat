from django.test import TestCase
from unittest import skip
from django.utils.html import escape

class HomepageTests(TestCase) :
    template_name = 'home.html'

    def test_uses_homepage_template(self) :
        response = self.client.get('/')
        self.assertTemplateUsed(response, self.template_name)

    def test_POST_valid_redirects_to_home_page(self) :
        response = self.client.post('/reading', data = { 'date' : '2019-03-12', 'reading' : '15' } )
        self.assertRedirects(response, '/')

    def test_POST_invalid_redirects_to_home_page(self) :
        response = self.client.post('/reading', data = { 'date' : '2019-03-12', 'reading' : '-15' } )
        self.assertRedirects(response, '/')

    def test_POST_invalid_displays_error_message(self) :
        response = self.client.post('/reading', data = { 'date' : '2019-03-12', 'reading' : '-15' } )
        self.assertContains(response, escape('The meter is not capable to display a negative electricity consumation, so a negative reading is not possible.'), status_code = 302)

    @skip
    def test_home_page_contains_correct_html(self) :
        pass

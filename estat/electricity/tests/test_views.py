from django.test import TestCase

class HomepageTests(TestCase) :
    def test_uses_homepage_template(self) :
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

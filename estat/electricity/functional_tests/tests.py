from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver import Firefox

class RegisterMeterReading(StaticLiveServerTestCase) :
    def setUp(self) :
        self.browser = Firefox()

    def tearDown(self) :
        self.browser.quit()

    def test_estat_page_is_online(self) :
        # alan opens the firefox web browser and enters the estat url
        # he sees it uses django
        self.browser.get('http://localhost:8000')
        self.assertIn('Electricity consumation statistics', self.browser.title, msg = 'Browser title is not correct')

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver import Firefox
from selenium.webdriver import Chrome
from .utilities import Logging


class RegisterMeterReading(StaticLiveServerTestCase) :

    def setUp(self) :
        self.browser = Firefox()
        self.browser.implicitly_wait(3)
        # self.browser = Chrome()

    def tearDown(self) :
        Logging.log_when_test_fails(self)
        self.browser.quit()

    def test_estat_page_is_online(self) :
        # alan opens the web browser and enters the estat url
        # he sees by the title on his browser that it's about electricity consumation statistics
        self.browser.get(self.live_server_url)
        self.assertIn('eElectricity consumation statistics', self.browser.title, msg = 'Browser title is not correct')

        # alan sees an edit box in which he can set a date
        # and he sees an edit box in which he can enter a number


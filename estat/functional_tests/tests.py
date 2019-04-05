from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver import Firefox
from selenium.webdriver import Chrome
from .utilities import Logging
from datetime import datetime
from selenium.webdriver.common.keys import Keys
from .utilities import BrowserUtilities


class RegisterMeterReading(StaticLiveServerTestCase) :

    def setUp(self) :
        self.browser = Firefox()
        self.browser.implicitly_wait(3)
        # self.browser = Chrome()

    def tearDown(self) :
        Logging.log_when_test_fails(self)
        self.browser.quit()

    '''----------------------------------------
    |     Use Case Register meter Reading     |
    ----------------------------------------'''
    def test_estat_page_is_online(self) :
        # alan opens the web browser and enters the estat url
        # he sees by the title on his browser that it's about Electricity consumation statistics
        self.browser.get(self.live_server_url)
        self.assertIn('Electricity consumation statistics', self.browser.title, msg = 'browser title is not correct')

    def test_input_reading(self) :
        '''
        happy path
        '''
        # alan opens his browsers and loads the estat url
        # he sees an edit box in which he can set a date
        self.browser.get(self.live_server_url)
        input_date = self.browser.find_element_by_id('input_date')
        self.assertIsNotNone(input_date, msg = 'no input_date input element')
        # and he sees an edit box in which he can enter a number
        input_reading = self.browser.find_element_by_id('input_reading')
        self.assertIsNotNone(input_reading, msg = 'no input_reading')

        # alan enters his first reading, 15 Kwh
        input_reading.send_keys('15')
        input_reading.send_keys(Keys.ENTER)
        # he sees an entry in the table with the date of today and next to it his freshly entered reading of 15 Kwh
        today = datetime.today()
        date_today = str(today)[:10]
        BrowserUtilities.wait_for_row_in_readings_table(self, date_today + ' 15')
        '''
        end happy path
        '''

        # he sees that the date in this edit box is the date of his computer
        # this formats the today variable to  YYYY-MM-DD
        self.assertEqual(date_today, input_date.get_attribute('value'), msg = 'default date is not set in date input')


        # alan decides to add another meter reading, this time with the date set to yesterday
        # alan decides to add another meter reading, this time with the date set to tomorrow

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver import Firefox
from selenium.webdriver import Chrome
from .utilities import Logging
from datetime import datetime
from selenium.webdriver.common.keys import Keys
from .utilities import BrowserUtilities
import time
from datetime import timedelta

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

    '''
    pre conditions
    '''
    def test_page_and_elements_are_available(self) :
        # alan opens the web browser and enters the estat url
        self.browser.get(self.live_server_url)

        # he sees by the title on his browser that it's about Electricity consumation statistics
        self.browser.get(self.live_server_url)
        self.assertIn('Electricity consumation statistics', self.browser.title, msg = 'browser title is not correct')

        # he sees an edit box in which he can set a date
        input_date = self.browser.find_element_by_id('id_date')
        self.assertIsNotNone(input_date, msg = 'no input for date')
        # he sees that the date in this edit box is the date of his computer
        # this formats the today variable to  YYYY-MM-DD
        today = datetime.today()
        date_today = str(today)[:10]
        input_date = self.browser.find_element_by_id('id_date')
        self.assertEqual(date_today, input_date.get_attribute('value'), msg = 'default date is not set in date input')

        # and he sees an edit box in which he can enter a number
        input_reading = self.browser.find_element_by_id('id_reading')
        self.assertIsNotNone(input_reading, msg = 'no input for meter reading')

    '''
    happy path
    '''
    def test_register_correct_meter_reading_and_date(self) :
        # alan opens the browser
        self.browser.get(self.live_server_url)
        input_date = self.browser.find_element_by_id('id_date')
        input_reading = self.browser.find_element_by_id('id_reading')

        # alan enters his first reading, 15 Kwh
        input_reading.send_keys('15')
        # he sees the date of today and next to it his freshly entered reading of 15 Kwh
        # nevertheless, he decides to enter a date by himself
        # first he clears the date field
        input_date.clear()
        # and then he fills in his date
        input_date.send_keys('2019-04-11')
        # next, he sees a submit button and presses it
        input_submit = self.browser.find_element_by_id('id_submit')
        self.assertIsNotNone(input_submit, msg = 'there is no submit button')
        input_submit.click()

        # alan now sees his entry in the table containing the readings
        BrowserUtilities.wait_for_row_in_readings_table(self, '2019-04-11 15.0')

    '''
    no date entered
    '''
    def test_register_correct_meter_reading_and_no_date(self) :
        # alan decides to add another meter reading, this time without setting the date himself
        # he opens the browser
        self.browser.get(self.live_server_url)

        # this time his reading is 20 Kwh
        input_reading = self.browser.find_element_by_id('id_reading')
        input_reading.send_keys('20')
        # he now accidently presses enter instead of the submit button
        input_reading.send_keys(Keys.ENTER)
        # he now sees both readings in the readings table and sees that the date is set to today
        # this formats the today variable to  YYYY-MM-DD
        today = datetime.today()
        date_today = str(today)[:10]
        BrowserUtilities.wait_for_row_in_readings_table(self, date_today + ' 20.0')

    '''
    date in the future entered
    '''
    def test_register_correct_meter_reading_and_date_in_the_future(self) :
        # alan decides to add another meter reading, this time with the date set to tomorrow
        # he opens the browser
        self.browser.get(self.live_server_url)

        # he enters 30kW as meter reading
        input_reading = self.browser.find_element_by_id('id_reading')
        input_reading.send_keys('30')
        # he enters the date of tomorrow as date
        # this formats the today variable to  YYYY-MM-DD
        tomorrow = datetime.today() + timedelta(days = 1)
        date_tomorrow = str(tomorrow)[:10]
        input_date = self.browser.find_element_by_id('id_date')
        # first he clears the date field
        input_date.clear()
        input_date.send_keys(date_tomorrow)
        # he presses submit
        input_submit = self.browser.find_element_by_id('id_submit')
        input_submit.click()

        # he sees an error message telling him he can not enter a date in the future
        list_items = BrowserUtilities.wait_for(lambda : self.browser.find_elements_by_tag_name('li'))
        self.assertIn('You can not submit a reading made in the future', [ list_item.text for list_item in list_items ], msg = 'error message not found in field date for date in the future')
        # the reading is not seen in the meter readings table
        BrowserUtilities.wait_for_row_not_in_readings_table(self, date_tomorrow + ' 30.0')

    '''
    wrong date format entered
    '''
    def test_register_correct_meter_reading_and_wrong_date_format(self) :
        pass

    '''
    no reading entered
    '''
    def test_register_no_reading_and_correct_date(self) :
        pass

    '''
    negative meter reading entered
    '''
    def test_register_negative_meter_reading_and_correct_date(self) :
        # alan decides to add another meter reading, this time with the date set to tomorrow
        # he opens the browser
        self.browser.get(self.live_server_url)

        # he enters -30kW as meter reading
        input_reading = self.browser.find_element_by_id('id_reading')
        input_reading.send_keys('-30')
        # he presses submit
        input_submit = self.browser.find_element_by_id('id_submit')
        input_submit.click()

        # he sees an error message telling him he can not enter a negative reading
        list_items = BrowserUtilities.wait_for(lambda : self.browser.find_elements_by_tag_name('li'))
        self.assertIn('The meter is not capable to display a negative electricity consumation, so a negative reading is not possible', [ list_item.text for list_item in list_items ], msg = 'error message not found in field reading for negative reading')
        # the reading is not seen in the meter readings table
        BrowserUtilities.wait_for_row_not_in_readings_table(self, str(datetime.today()) + ' 30.0')

    '''
    wrong format meter reading entered
    '''
    def test_register_wrong_meter_reading_format_and_correct_date(self) :
        pass

    '''
    negative meter reading entered and wrong date format entered
    '''
    def test_register_negative_meter_reading_and_wrong_date_format(self) :
        pass

    '''
    multiple correct readings enetered
    '''
    def test_register_multiple_correct_readings(self) :
        pass

    '''--------------------------------------------
    |     End Use Case Register meter Reading     |
    --------------------------------------------'''

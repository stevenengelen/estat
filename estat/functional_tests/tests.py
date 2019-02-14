from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver import Firefox
from selenium.webdriver import Chrome
import os
import time

SCREEN_DUMP_LOCATION = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'screendumps')

class RegisterMeterReading(StaticLiveServerTestCase) :
    def setUp(self) :
        self.browser = Firefox()
        self.browser.implicitly_wait(3)
        # self.browser = Chrome()

    def tearDown(self) :
        self.browser.quit()
        '''
        if self._test_has_failed() :
            if not os.path.exists(SCREEN_DUMP_LOCATION) :
                os.makedirs(SCREEN_DUMP_LOCATION)
            for ix, handle in enumerate(self.browser.window_handles) :
                self._windowid = ix
                self.browser.switch_to_window(handle)
                self.take_screenshot()
                self.dump_html()
        self.browser.quit()
        super().tearDown()
        '''

    def _test_has_failed(self) :
        # slighty obscure but couldn't find a better way!
        return any(error for (method, error) in self._outcome.errors)

    def take_screenshot(self) :
        filename = self._get_filename() + '.png'
        print('screenshotting to', filename)
        self.browser.get_screenshot_as_file(filename)

    def dump_html(self) :
        filename = self._get_filename() + '.html'
        print('dumping page HTML to', filename)
        with open(filename, 'w') as f :
            f.write(self.browser.page_source)

    def _get_filename(self) :
        timestamp = datetime.now().isoformat().replace(':', '.')[:19]
        return '{folder}/{classname}.{method}.window{windowid}-{timestamp}'.format(
                folder = SCREEN_DUMP_LOCATION,
                classname = self.__class__.__name__,
                method = self._testMethodName,
                windowid = self._windowid,
                timestamp = timestamp
                )

    def test_estat_page_is_online(self) :
        # alan opens the web browser and enters the estat url
        # he sees by the title on his browser that it's about electricity consumation statistics
        self.browser.get(self.live_server_url)
        print(self.browser.title)
        time.sleep(10)
        self.assertIn('Electricity consumation statistics', self.browser.title, msg = 'Browser title is not correct')

        # alan sees an edit box in which he can set a date
        # and he sees an edit box in which he can enter a number


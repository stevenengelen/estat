import os
from datetime import datetime
import time
from selenium.common.exceptions import WebDriverException

SCREEN_DUMP_LOCATION = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'screendumps')
MAX_WAIT = 10

def wait(fn) :
    def modified_fn(*args, **kwargs) :
        start_time = time.time()
        while True :
            try :
                return fn(*args, **kwargs)
            except (AssertionError, WebDriverException) as e :
                if time.time() - start_time > MAX_WAIT :
                    raise e
                time.sleep(0.5)
    return modified_fn

class Logging(object) :

    @staticmethod
    def log_when_test_fails(testclass) :
        Logging.testclass = testclass
        if Logging._test_has_failed() :
            if not os.path.exists(SCREEN_DUMP_LOCATION) :
                os.makedirs(SCREEN_DUMP_LOCATION)
            for ix, handle in enumerate(Logging.testclass.browser.window_handles) :
                Logging.testclass._windowid = ix
                Logging.testclass.browser.switch_to_window(handle)
                Logging.take_screenshot()
                Logging.dump_html()

    @staticmethod
    def _test_has_failed() :
        return any(error for (method, error) in Logging.testclass._outcome.errors)

    @staticmethod
    def take_screenshot() :
        filename = Logging._get_filename() + '.png'
        print('screenshotting to', filename)
        Logging.testclass.browser.get_screenshot_as_file(filename)

    @staticmethod
    def dump_html() :
        filename = Logging._get_filename() + '.html'
        print('dumping page HTML to', filename)
        with open(filename, 'w') as f :
            f.write(Logging.testclass.browser.page_source)

    @staticmethod
    def _get_filename() :
        timestamp = datetime.now().isoformat().replace(':', '.')[:19]
        return '{folder}/{classname}.{method}.window{windowid}-{timestamp}'.format(
                folder = SCREEN_DUMP_LOCATION,
                classname = Logging.testclass.__class__.__name__,
                method = Logging.testclass._testMethodName,
                windowid = Logging.testclass._windowid,
                timestamp = timestamp
                )

class BrowserUtilities(object) :

    @staticmethod
    @wait
    def wait_for_row_in_readings_table(test_class, row_text) :
        readings = test_class.browser.find_element_by_id('id_table_readings')
        rows = readings.find_elements_by_tag_name('tr')
        test_class.assertIn(row_text, [row.text for row in rows])

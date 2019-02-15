import os
from datetime import datetime

SCREEN_DUMP_LOCATION = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'screendumps')

class Logging(object) :

    @staticmethod
    def log_when_test_fails(testclass) :
        Logging.testclass = testclass
        if Logging._test_has_failed() :
            print('-----in Logging.log_when_test_fails() path test_has_failed()')
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

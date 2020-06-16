from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from django.test import LiveServerTestCase
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
import time

MAX_WAIT = 5

class FunctionalTest(StaticLiveServerTestCase):
    def setUp(self):
        options = webdriver.firefox.options.Options()
        options.headless = True
        self.browser = webdriver.Firefox(options=options)

    def tearDown(self):
        self.browser.quit()

    def wait_for(self, assertion):
        start_time = time.time()
        while True:
            try:
                return assertion()
            except (AssertionError,WebDriverException)  as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(.5)
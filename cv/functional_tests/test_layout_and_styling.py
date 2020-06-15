from .base import FunctionalTest
import time

class LayoutAndStylingTest(FunctionalTest):
    def test_user_visits_site_and_can_read_info(self):
        # Ani has heard about a cool ML developer, tornikeo.
        # She goes to check out his homepage.
        # self.browser.get(self.live_server_url)
        self.browser.get('http://localhost:8000')

        # She notices the name of the develoepr on page title
        self.assertIn('Tornike', self.browser.title)

        # She sees a picture of the dev

        # She sees the name "TornikeO"

        # There is email link. The email link redirects
        # To email service. email is "tonop15@freeuni.edu.ge"

        # She closes the email tab and returns to
        # scroll down more.

        # She sees a "Reasearch" header. There are two entries.

        # She sees an Experience header.

        # Satisfied she goes to sleep.
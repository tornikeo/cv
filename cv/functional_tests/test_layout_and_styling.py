from .base import FunctionalTest
import time

class LayoutAndStylingTest(FunctionalTest):
    def test_user_visits_site_and_can_read_info(self):
        # Ani has heard about a cool ML developer, tornikeo.
        # She goes to check out his homepage.
        # self.browser.get(self.live_server_url)
        self.browser.get('http://localhost:8000')
        self.browser.set_window_size(1024, 768)

        # She notices the name of the develoepr on page title
        self.assertIn('Tornike', self.browser.title)

        # She sees a picture of the dev
        self.wait_for(lambda: self.browser.find_element_by_id("id_picture"))

        # She sees the name "TornikeO"
        header_text = self.wait_for(lambda: 
            self.browser.find_element_by_tag_name("h1")
        )
        self.assertIn('TornikeO', header_text)

        # There is email link. The email link redirects
        # To email service. email is "tonop15@freeuni.edu.ge"
        email_link_tag = self.wait_for(
            lambda: self.browser.find_elements_by_id('id_email')
        )
        self.assertIn(
            "tonop15@freeuni.edu.ge",
            email_link_tag.get_attribute("href")
        )
        self.fail("Finish test!")
        # She closes the email tab and returns to
        # scroll down more.

        # She sees a "Reasearch" header. There are two entries.

        # She sees an Experience header.

        # Satisfied she goes to sleep.
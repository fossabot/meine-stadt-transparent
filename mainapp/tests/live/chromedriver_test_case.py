from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.chrome.options import Options
from django.test import modify_settings
from splinter import Browser

chromedriver_path = "node_modules/.bin/chromedriver"


"""
Specifics of ChromeDriverTestCase:
- Chrome Headless is used
- English is used for the UI
- CSRF-checks are disabled, as referrer-checking seems to be problematic, as the HTTPS-header seems to be always set
"""


@modify_settings(MIDDLEWARE={
    'remove': ['django.middleware.csrf.CsrfViewMiddleware'],
})
class ChromeDriverTestCase(StaticLiveServerTestCase):
    browser = None

    @classmethod
    def setUpClass(cls):
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': 'en_US'})
        cls.browser = Browser('chrome', headless=True, executable_path="node_modules/.bin/chromedriver", options=options)
        super(ChromeDriverTestCase, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()
        super(ChromeDriverTestCase, cls).tearDownClass()

    """
    Helper functions for a more convenient test syntax
    """

    def assertTextIsPresent(self, text):
        self.assertTrue(self.browser.is_text_present(text))

    def assertTextIsNotPresent(self, text):
        self.assertFalse(self.browser.is_text_present(text))

    def assertElementDoesExists(self, css_selector):
        self.assertTrue(self.browser.is_element_present_by_css(css_selector))

    def assertElementDoesNotExists(self, css_selector):
        self.assertFalse(self.browser.is_element_present_by_css(css_selector))

    """
    Functions for behaviors used by several test cases
    """

    def logout(self):
        self.browser.find_by_css('#main-menu-content .my-account-link').click()
        self.browser.find_by_css('.logout-form button').click()
        self.assertTextIsPresent('You have signed out.')
        self.assertElementDoesExists('#main-menu-content .login-link')
        self.assertElementDoesNotExists('#main-menu-content .my-account-link')

    def login(self, username, password):
        self.browser.find_by_css('#main-menu-content .login-link').click()
        self.browser.fill('login', username)
        self.browser.fill('password', password)
        self.browser.find_by_css('form.login button').click()
        self.assertTextIsPresent('Successfully signed in as ' + username)
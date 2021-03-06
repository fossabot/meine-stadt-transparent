import time

from mainapp.tests.live.chromedriver_test_case import ChromeDriverTestCase


class PersonsTest(ChromeDriverTestCase):
    fixtures = ['initdata.json']

    def _get_pos_by_name(self, name):
        js = 'window.jQuery(".persons-list").data("get-item-pos-by-name")("' + name + '");'
        pos = self.browser.evaluate_script(js)
        return pos

    def test_filter(self):
        self.browser.visit('%s%s' % (self.live_server_url, '/persons/'))

        # Both are visible
        pos_peter = self._get_pos_by_name('Peter Russo')
        pos_hector = self._get_pos_by_name('Hector Mendoza')
        self.assertIsNotNone(pos_peter)
        self.assertIsNotNone(pos_hector)

        # Filter for democrats
        self.browser.find_by_css('.filter-organizations .organization-6').first.click()
        time.sleep(1)
        pos_peter = self._get_pos_by_name('Peter Russo')
        pos_hector = self._get_pos_by_name('Hector Mendoza')
        self.assertIsNotNone(pos_peter)
        self.assertIsNone(pos_hector)

        # Filter for republicans
        self.browser.find_by_css('.filter-organizations .organization-7').first.click()
        time.sleep(1)
        pos_peter = self._get_pos_by_name('Peter Russo')
        pos_hector = self._get_pos_by_name('Hector Mendoza')
        self.assertIsNone(pos_peter)
        self.assertIsNotNone(pos_hector)

    def test_sort(self):
        self.browser.visit('%s%s' % (self.live_server_url, '/persons/'))

        # Default sorting: by name
        pos_peter = self._get_pos_by_name('Peter Russo')
        pos_hector = self._get_pos_by_name('Hector Mendoza')
        self.assertLess(pos_hector, pos_peter)

        # Switch to sorting by party
        self.browser.find_by_css('#btnSortDropdown').first.click()
        self.browser.find_by_css('.sort-selector a[data-sort="group"]').first.click()
        time.sleep(1)
        pos_peter = self._get_pos_by_name('Peter Russo')
        pos_hector = self._get_pos_by_name('Hector Mendoza')
        self.assertLess(pos_peter, pos_hector)

        # Switch back to sorting by name
        self.browser.find_by_css('#btnSortDropdown').first.click()
        self.browser.find_by_css('.sort-selector a[data-sort="name"]').first.click()
        time.sleep(1)
        pos_peter = self._get_pos_by_name('Peter Russo')
        pos_hector = self._get_pos_by_name('Hector Mendoza')
        self.assertLess(pos_hector, pos_peter)

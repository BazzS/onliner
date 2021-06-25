from selenium import webdriver
import allure
import unittest

from onliner import SearchOnliner

class PlayGround(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)

    @allure.feature("Test Onliner")
    @allure.story("Equal price")
    def test_onliner(self):
        browser = self.driver
        page = SearchOnliner(browser)
        with allure.step('Go main page'):
            page.go_to_site()
        with allure.step('Go catalog'):
            page.go_catalog()
        with allure.step('Go electronic'):
            page.go_electronic()
        with allure.step('Go electorinc category'):
            page.go_mobile()
        with allure.step('Select mobiles'):
            page.click_phones()
        with allure.step('Click test phone'):
            page.select_phone()
        with allure.step('Search test phone price'):
            price = page.find_price()
        with allure.step('Get test phone name'):
            phone_name = page.get_name()
        with allure.step('Search test phone by name'):
            page.search_area(phone_name)
        with allure.step('Switch to iframe'):
            page.switch_iframe()
        with with allure.step('Search test phone price'):
            iframe_price = page.price_iframe()
        self.assertEqual(price, iframe_price)

    def tearDown(self):
        self.driver.quit()

from base import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class Locators:
    CATALOG = (By.CLASS_NAME, "b-main-navigation__link")
    ELECTRONIC = (By.CLASS_NAME, "catalog-navigation-classifier__item")
    PHONES_ACCESSORIES = (By.XPATH, "//*[@id="container"]/div/div/div/div/div[1]/div[3]/div/div[1]/div[1]/div/div[1]/div[1]")
    PHONES = (By.XPATH, "//*[@id="container"]/div/div/div/div/div[1]/div[3]/div/div[1]/div[1]/div/div[1]/div[2]/div/a[1]")
    TEST_PHONE = (By.XPATH, "//*[@id="schema-products"]/div[2]/div/div[3]/div[2]/div[1]/a/span")
    PRICE = (By.XPATH, "//*[@id="container"]/div/div/div/div/div[2]/div[1]/main/div/div/div[1]/div[2]/div[5]/div[1]/div/a")
    INPUT = (By.XPATH, "//*[@id="fast-search"]/form/input[1]")
    PHONE_NAME = (By.XPATH, "//*[@id="container"]/div/div/div/div/div[2]/div[1]/div/div[4]/h1")
    IFRAME = (By.CLASS_NAME, "modal-iframe")
    PRICE_IFRAME = (By.XPATH, "//div[@id='search-page']/div[@class='search__content-wrapper']/"
                              "ul[@class='search__results']/li[1]//div[@class='product__price']/a[1]/span")

class SearchOnliner(Base):
    def go_catalog(self):
        return self.find_element(Locators.CATALOG, time=2).click()

    def go_electronic(self):
        return self.find_element(Locators.ELECTRONIC, time=2).click()

    def go_mobile(self):
        phones = self.find_element(Locators.PHONES_ACCESSORIES, time=2)
        move_to_element = ActionChains(self.driver).move_to_element(phones)
        return move_to_element.perform()

    def click_phones(self):
        return self.find_element(Locators.PHONES, time=2).click()

    def select_phone(self):
        return self.find_element(LOCATORS.TEST_PHONE, time=2).click()

    def get_name(self):
        return self.find_element(LOCATORS.PHONE_NAME, time=2).text

    def find_price(self):
        return self.find_element(LOCATORS.PRICE, time=2).text

    def search_area(self, search_text)
        return self.find_element(LOCATORS.INPUT, time=2).send_keys(f'{search_text}')

    def switch_iframe(self):
        iframe = self.find_element(Locators.IFRAME, time=2)
        return self.driver.switch_iframe(iframe)

    def price_iframe(self):
        return self.find_element(Locators.PRICE_IFRAME, time=2).text

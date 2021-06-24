from base import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class Locators:
    LINK_CATALOG = (By.CLASS_NAME, "b-main-navigation__link")
    LINK_ELECTRONIC = (By.CLASS_NAME, "catalog-navigation-classifier__item")
    PHONES_ACCESSORIES = (By.XPATH, "//*[@id="container"]/div/div/div/div/div[1]/div[3]/div/div[1]/div[1]/div/div[1]/div[1]")
    PHONES = (By.XPATH, "//*[@id="container"]/div/div/div/div/div[1]/div[3]/div/div[1]/div[1]/div/div[1]/div[2]/div/a[1]"")
    

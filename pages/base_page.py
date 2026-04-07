import allure

from abc import ABC

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import (
    presence_of_element_located,
    element_to_be_clickable
) 


class BasePage(ABC):
    def __init__(self, driver):
        self.driver = driver 

    @allure.step("Открытие страницы {url}")
    def open(self, url):
        self.driver.get(url)

    @allure.step("Ожидание получения заголовка страницы")
    def get_title(self):
        return self.driver.title

    @allure.step("Ожидание элемента на странице {locator}")
    def wait_presense_of_element_to_located(self, locator):
        return WebDriverWait(self.driver, 10).until(
            presence_of_element_located(locator)
        )
    
    @allure.step("Ожидание кликабельности элемента")
    def wait_until_button_clickable(self, locator):
        return WebDriverWait(self.driver, 10).until(
            element_to_be_clickable(locator)
        )

    @allure.step("Клик по заданному элементу")
    def click(self, locator):
        self.wait_until_button_clickable(locator)
        self.driver.find_element(*locator).click()
    
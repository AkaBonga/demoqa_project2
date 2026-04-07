import allure
import data

from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AlertsPage(BasePage):
    H1 = (By.TAG_NAME, "h1")

    @allure.step("Получение заголовка страницы Alerts")
    def get_title_from_h1(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.presence_of_element_located(self.H1))
        return element.text
    
    @allure.step("Проверка корректности Title")
    def is_title_on_page_correct(self):
        actual_title = self.get_title_from_h1()
        expected_title = data.AlertPagesData.H1
        return actual_title == expected_title
import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ElementsPage(BasePage):

    ELEMENTS_CARD = (By.XPATH, "//div[contains(@class,'top-card')][.//h5[text()='Elements']]")
    TEXT_BOX_MENU = (By.XPATH, "//span[text()='Text Box']")

    FULL_NAME_INPUT = (By.ID, "userName")
    EMAIL_INPUT = (By.ID, "userEmail")
    CURRENT_ADDRESS_INPUT = (By.ID, "currentAddress")
    PERMANENT_ADDRESS_INPUT = (By.ID, "permanentAddress")
    SUBMIT_BUTTON = (By.ID, "submit")

    OUTPUT_NAME = (By.ID, "name")
    OUTPUT_EMAIL = (By.ID, "email")
    OUTPUT_CURRENT_ADDRESS = (By.XPATH, "//p[@id='currentAddress']")
    OUTPUT_PERMANENT_ADDRESS = (By.XPATH, "//p[@id='permanentAddress']")

    @allure.step("Кликаем по карточке Elements")
    def click_elements_card(self):
        element = self.wait_presense_of_element_to_located(ElementsPage.ELEMENTS_CARD)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        element.click()

    @allure.step("Открываем пункт Text Box")
    def open_text_box(self):
        # Находим элемент и прокручиваем к нему перед кликом
        element = self.driver.find_element(*ElementsPage.TEXT_BOX_MENU)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        element.click()

    @allure.step("Заполняем поле Full Name")
    def enter_full_name(self, full_name):
        element = self.driver.find_element(*ElementsPage.FULL_NAME_INPUT)
        element.clear()
        element.send_keys(full_name)

    @allure.step("Заполняем поле Email")
    def enter_email(self, email):
        element = self.driver.find_element(*ElementsPage.EMAIL_INPUT)
        element.clear()
        element.send_keys(email)

    @allure.step("Заполняем поле Current Address")
    def enter_current_address(self, current_address):
        element = self.driver.find_element(*ElementsPage.CURRENT_ADDRESS_INPUT)
        element.clear()
        element.send_keys(current_address)

    @allure.step("Заполняем поле Permanent Address")
    def enter_permanent_address(self, permanent_address):
        element = self.driver.find_element(*ElementsPage.PERMANENT_ADDRESS_INPUT)
        element.clear()
        element.send_keys(permanent_address)

    @allure.step("Нажимаем кнопку Submit")
    def click_submit(self):
        self.wait_until_button_clickable(ElementsPage.SUBMIT_BUTTON)
        submit_button = self.driver.find_element(*ElementsPage.SUBMIT_BUTTON)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", submit_button)
        self.driver.execute_script("window.scrollBy(0, -200);")
        self.driver.execute_script("arguments[0].click();", submit_button)

    @allure.step("Проверяем, что блок с результатами отображается")
    def is_output_displayed(self):
        return self.driver.find_element(*ElementsPage.OUTPUT_NAME).is_displayed()

    @allure.step("Получаем class у поля Email")
    def get_email_input_class(self):
        return self.driver.find_element(*ElementsPage.EMAIL_INPUT).get_attribute("class")
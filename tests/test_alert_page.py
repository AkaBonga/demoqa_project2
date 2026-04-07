import pytest
import allure
import data
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    """Фикстура для браузера"""
    options = webdriver.ChromeOptions()
    options.add_argument('--start-maximized')
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_argument('--disable-popup-blocking')
    
    service = Service(r'C:\is30\demoqa_project\chromedriver-win64\chromedriver.exe')
    
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()


@allure.feature('Тестирование страницы Alerts')
class TestPracticeFormPage:

    @allure.title("Проверка доступности страницы Alerts")
    @allure.description("Проверка осуществляется по заголовку H1 на странице")
    def test_alert_page_title(self, driver):
        # Открываем страницу
        url = data.BASE_URL + data.ALERTS_WINDOW_URL
        driver.get(url)
        
        # Ждем загрузки страницы
        time.sleep(3)
        
        # Выводим информацию для отладки
        print(f"\nТекущий URL: {driver.current_url}")
        print(f"Заголовок страницы (title): {driver.title}")
        
        # Пробуем найти H1 разными способами
        wait = WebDriverWait(driver, 10)
        
        # Способ 1: По тегу h1
        try:
            h1_element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "h1")))
            actual_h1 = h1_element.text
            print(f"Найден H1 (по тегу): '{actual_h1}'")
        except:
            print("H1 по тегу не найден")
            actual_h1 = ""
        
        # Способ 2: По CSS селектору
        if not actual_h1:
            try:
                h1_element = driver.find_element(By.CSS_SELECTOR, "h1")
                actual_h1 = h1_element.text
                print(f"Найден H1 (по CSS): '{actual_h1}'")
            except:
                print("H1 по CSS не найден")
        
        # Способ 3: По XPath
        if not actual_h1:
            try:
                h1_element = driver.find_element(By.XPATH, "//h1")
                actual_h1 = h1_element.text
                print(f"Найден H1 (по XPath): '{actual_h1}'")
            except:
                print("H1 по XPath не найден")
        
        # Проверяем, что нашли текст
        expected_h1 = data.AlertPagesData.H1
        print(f"Ожидаемый H1: '{expected_h1}'")
        
        with allure.step('Проверка что заголовок правильный'):
            assert actual_h1 == expected_h1, \
                f"Заголовок страницы не соответствует. Ожидалось: '{expected_h1}', Получено: '{actual_h1}'"


if __name__ == "__main__":
    pytest.main(["-v", "-s", __file__])
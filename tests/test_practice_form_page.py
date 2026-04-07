import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def driver():
    """Фикстура для браузера"""
    options = webdriver.ChromeOptions()
    options.add_argument('--start-maximized')
    # Добавляем опцию для игнорирования ошибок с перекрытием
    options.add_argument('--disable-blink-features=AutomationControlled')
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )
    yield driver
    driver.quit()

def test_practice_form(driver):
    """Тест заполнения формы"""
    driver.get("https://demoqa.com/automation-practice-form")
    wait = WebDriverWait(driver, 10)
    
    # Сначала закроем рекламный баннер, если он есть
    try:
        close_ads = driver.find_element(By.ID, "close-fixedban")
        driver.execute_script("arguments[0].click();", close_ads)
        time.sleep(0.5)
    except:
        pass
    
    # Прокручиваем страницу вверх, чтобы убрать перекрытие
    driver.execute_script("window.scrollTo(0, 0);")
    time.sleep(0.5)
    
    # Заполнение формы
    driver.find_element(By.ID, "firstName").send_keys("Иван")
    driver.find_element(By.ID, "lastName").send_keys("Петров")
    driver.find_element(By.ID, "userEmail").send_keys("test@example.com")
    
    # Выбор пола
    driver.execute_script("arguments[0].click();", driver.find_element(By.XPATH, "//label[text()='Male']"))
    
    # Телефон
    driver.find_element(By.ID, "userNumber").send_keys("1234567890")
    
    # Дата рождения
    driver.find_element(By.ID, "dateOfBirthInput").click()
    time.sleep(0.5)
    
    # Выбор года
    year_select = driver.find_element(By.CLASS_NAME, "react-datepicker__year-select")
    driver.execute_script("arguments[0].click();", year_select)
    driver.execute_script("arguments[0].click();", year_select.find_element(By.XPATH, "//option[@value='1990']"))
    
    # Выбор месяца
    month_select = driver.find_element(By.CLASS_NAME, "react-datepicker__month-select")
    driver.execute_script("arguments[0].click();", month_select)
    driver.execute_script("arguments[0].click();", month_select.find_element(By.XPATH, "//option[text()='May']"))
    
    # Выбор дня
    day_element = driver.find_element(By.XPATH, "//div[@class='react-datepicker__day react-datepicker__day--015']")
    driver.execute_script("arguments[0].click();", day_element)
    
    # Предметы
    subjects = driver.find_element(By.ID, "subjectsInput")
    subjects.send_keys("Maths")
    subjects.send_keys(Keys.RETURN)
    subjects.send_keys("English")
    subjects.send_keys(Keys.RETURN)
    
    # Хобби - используем JavaScript для клика
    hobbies = ["Sports", "Reading"]
    for hobby in hobbies:
        element = driver.find_element(By.XPATH, f"//label[text()='{hobby}']")
        driver.execute_script("arguments[0].click();", element)
    
    # Адрес
    driver.find_element(By.ID, "currentAddress").send_keys("Тестовый адрес, г. Москва")
    
    # Прокручиваем до элемента State
    state_input = driver.find_element(By.ID, "react-select-3-input")
    driver.execute_script("arguments[0].scrollIntoView(true);", state_input)
    time.sleep(0.5)
    
    # Штат и город
    state_input.send_keys("NCR")
    state_input.send_keys(Keys.RETURN)
    
    city_input = driver.find_element(By.ID, "react-select-4-input")
    city_input.send_keys("Delhi")
    city_input.send_keys(Keys.RETURN)
    
    # Важное решение для кнопки Submit:
    # Способ 1: Клик через JavaScript (самый надёжный)
    submit_button = driver.find_element(By.ID, "submit")
    driver.execute_script("arguments[0].scrollIntoView(true);", submit_button)
    time.sleep(0.5)
    driver.execute_script("arguments[0].click();", submit_button)
    
    # Ждём появления модального окна
    time.sleep(2)
    
    # Проверяем успешную отправку
    try:
        modal_title = wait.until(EC.presence_of_element_located((By.ID, "example-modal-sizes-title-lg")))
        assert "Thanks for submitting the form" in modal_title.text
        print("\n✅ ТЕСТ ПРОЙДЕН УСПЕШНО! Форма отправлена.")
        
        # Делаем скриншот
        driver.save_screenshot("form_success.png")
        print("📸 Скриншот сохранён как form_success.png")
        
    except:
        # Альтернативная проверка
        modal_text = driver.find_element(By.CLASS_NAME, "modal-content").text
        assert "Thanks for submitting" in modal_text
        print("\n✅ ТЕСТ ПРОЙДЕН УСПЕШНО!")

if __name__ == "__main__":
    pytest.main(["-v", "-s", __file__])
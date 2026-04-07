import chromedriver_autoinstaller
import pytest
from selenium import webdriver


@pytest.fixture(scope='function')
def driver():
    chromedriver_autoinstaller.install() 
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

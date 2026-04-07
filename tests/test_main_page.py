import allure

import data
from pages.main_page import MainPage


@allure.feature("Тестирование главной страницы")
class TestMainPage:
    
    @allure.title("Проверка доступности главной страницы")
    @allure.description("Проверка осуществляется по соответствию названию заголовка заданного значения")
    def test_main_page_is_available(self, driver):
        main_page = MainPage(driver)
        main_page.open(data.BASE_URL)
        
        with allure.step("Проверка заголовка"):
            assert main_page.get_title() == 'demosite'

    @allure.title("Проверка количества карточек на странице = 6")
    @allure.description("На странице должно располагаться 6 карточек")
    def test_number_of_cards_is_6(self, driver):
        main_page = MainPage(driver)
        main_page.open(data.BASE_URL)

        with allure.step("Проверка количества карточек"):
            assert main_page.get_number_cards() == 6
        
    @allure.title("При клике на лого открывается стартовая страница")
    @allure.description("При клике должна открываться стартовая страница")
    def test_click_on_logo_go_to_main_page(self, driver):
        """
        1. Открыть страницу заданным url
        2. Подождать пока загрузится
        3. Нашли лого
        4. Кликнуть по лого
        5. Проверить что title соответствует ожидаемому значению
        """
        main_page = MainPage(driver)
        main_page.open(data.BASE_URL)
        main_page.click_on_logo()

        with allure.step("Title соответствует ожиданию"):
            assert main_page.get_title() == 'demosite'

    @allure.title("Проверка название 1-ой карточки")
    @allure.description("Название 1-ой карточки соответствует названию на сайте")
    def test_name_first_card_is_element(self, driver):
        """
        1. Открыть страницу заданным url
        2. Подождать пока загрузится
        3. Находим первую карточку
        4. Проверить что название карточки соответствует ожиданию
        """
        main_page = MainPage(driver)
        main_page.open(data.BASE_URL)

        with allure.step("Название первой карточки соответствует ожидаемому"):
            assert main_page.is_card_with_name()

    @allure.title("Проверка название 2-ой карточки")
    @allure.description("Название 2-ой карточки соответствует названию на сайте")
    def test_name_second_card_is_forms(self, driver):
        """
        1. Открыть страницу заданным url
        2. Подождать пока загрузится
        3. Находим первую карточку
        4. Проверить что название карточки соответствует ожиданию
        """
        main_page = MainPage(driver)
        main_page.open(data.BASE_URL)

        with allure.step("Название второй карточки соответствует ожидаемому"):
            assert main_page.is_card_with_name_forms()

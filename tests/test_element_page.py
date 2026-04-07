import allure
import data
from pages.elements_page import ElementsPage


@allure.feature("Тестирование страницы Elements")
class TestElementsPage:

    @allure.title("Проверка открытия страницы Text Box")
    @allure.description("При клике на карточку Elements и пункт Text Box открывается страница Text Box")
    def test_open_text_box(self, driver):
        """
        1. Открыть главную страницу
        2. Кликнуть по карточке Elements
        3. Кликнуть по пункту Text Box
        4. Проверить url
        """
        page = ElementsPage(driver)
        page.open(data.BASE_URL)

        page.click_elements_card()
        page.open_text_box()

        with allure.step("Проверка url страницы"):
            assert "text-box" in driver.current_url

    @allure.title("Проверка заполнения формы Text Box")
    @allure.description("После заполнения формы и нажатия Submit отображается блок с введёнными данными")
    def test_fill_text_box(self, driver):
        """
        1. Открыть главную страницу
        2. Кликнуть по карточке Elements
        3. Открыть Text Box
        4. Заполнить поля
        5. Нажать Submit
        6. Проверить отображение результата
        """
        page = ElementsPage(driver)
        page.open(data.BASE_URL)

        page.click_elements_card()
        page.open_text_box()
        page.enter_full_name("Vetrov SAnya")
        page.enter_email("sanya@lanos.com")
        page.enter_current_address("Tambow")
        page.enter_permanent_address("Russia")
        page.click_submit()

        with allure.step("Проверка отображения результата"):
            assert page.is_output_displayed()

    @allure.title("Проверка невалидного email в Text Box")
    @allure.description("При вводе невалидного email поле должно получить класс ошибки")
    def test_invalid_email(self, driver):
        """
        1. Открыть главную страницу
        2. Кликнуть по карточке Elements
        3. Открыть Text Box
        4. Ввести невалидный email
        5. Нажать Submit
        6. Проверить class поля email
        """
        page = ElementsPage(driver)
        page.open(data.BASE_URL)

        page.click_elements_card()
        page.open_text_box()
        page.enter_full_name("Vetrov Sanya")
        page.enter_email("invalid_email")
        page.enter_current_address("Tambow")
        page.enter_permanent_address("Russia")
        page.click_submit()

        with allure.step("Проверка ошибки в поле Email"):
            assert "field-error" in page.get_email_input_class()
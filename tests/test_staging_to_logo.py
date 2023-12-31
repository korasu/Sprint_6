import allure
from pages.main_page import MainPage
from locators.locators_for_base_page import LocatorsBasePage


class TestLogo:
    @allure.title("Тест на открытие страницы 'Яндекса'")
    def test_click_yandex_logo(self, driver):
        main_page = MainPage(driver)

        main_page.open_site()
        main_page.click_yandex_logo()
        main_page.switch_tab()
        main_page.wait_need_element(LocatorsBasePage.banner_yandex_browser, 10)
        current_url = main_page.get_current_url()

        assert "dzen.ru" in current_url

    @allure.title("Тест на переход на главную страницу 'Яндекс Самоката'")
    def test_click_scooter_logo(self, driver):
        main_page = MainPage(driver)

        main_page.open_site()
        main_page.click_header_ordering_button()
        main_page.click_scooter_logo()
        current_url = main_page.get_current_url()

        assert "https://qa-scooter.praktikum-services.ru/" == current_url

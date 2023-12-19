import allure
from pages.main_page import MainPage
from pages.base_page import BasePage
from locators.locators_for_base_page import LocatorsBasePage


class TestLogo:
    @allure.title("Тест на открытие страницы 'Яндекса'")
    def test_click_yandex_logo(self, driver):
        base_page = BasePage(driver)
        base_page.open_site()
        main_page = MainPage(driver)
        main_page.click_yandex_logo()
        base_page.switch_tab()
        base_page.wait_need_element(LocatorsBasePage.banner_yandex_browser, 10)
        current_url = base_page.get_current_url()

        assert "dzen.ru" in current_url

    @allure.title("Тест на переход на главную страницу 'Яндекс Самоката'")
    def test_click_scooter_logo(self, driver):
        base_page = BasePage(driver)
        base_page.open_site()
        main_page = MainPage(driver)
        main_page.click_header_ordering_button()
        main_page.click_scooter_logo()
        current_url = base_page.get_current_url()

        assert "scooter" in current_url

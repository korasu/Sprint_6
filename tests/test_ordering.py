import allure
from pages.main_page import MainPage
from pages.base_page import BasePage
from pages.ordering_page import OrderingPage
from locators.locators_for_ordering_page import LocatorsOrderingPage
from data import Data


class TestOrdering:
    @allure.title("Тест на оформление заказа с помощью кнопки в хэдоре страницы")
    def test_ordering_with_header_button(self,driver):
        main_page = MainPage(driver)

        main_page.open_site()
        main_page.click_cookie_button()
        main_page.click_header_ordering_button()

        order_page = OrderingPage(driver)

        order_page.filling_order(Data.metro1, LocatorsOrderingPage.first_data,
                                 LocatorsOrderingPage.first_rent_time, LocatorsOrderingPage.black_scooter)

        assert "Заказ оформлен" in order_page.get_text_order()

    @allure.title("Тест на оформление заказа с помощью кнопки в конце страницы")
    def test_ordering_with_bottom_button(self, driver):
        main_page = MainPage(driver)

        main_page.open_site()
        main_page.click_cookie_button()
        main_page.click_bottom_ordering_button()

        order_page = OrderingPage(driver)

        order_page.filling_order(Data.metro2, LocatorsOrderingPage.second_data,
                                 LocatorsOrderingPage.second_rent_time, LocatorsOrderingPage.grey_scooter)

        assert "Заказ оформлен" in order_page.get_text_order()

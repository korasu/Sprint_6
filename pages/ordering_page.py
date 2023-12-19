import allure
from locators.locators_for_ordering_page import LocatorsOrderingPage
from pages.base_page import BasePage
from data import Data


class OrderingPage(BasePage):
    @allure.step('Заполнение обязательных полей для заказа')
    def filling_order(self, metro_data, date, rent, color):
        self.driver.find_element(*LocatorsOrderingPage.name_input).send_keys(Data.name)

        self.driver.find_element(*LocatorsOrderingPage.second_name_input).send_keys(Data.second_name)

        self.driver.find_element(*LocatorsOrderingPage.address_input).send_keys(Data.address)

        self.driver.find_element(*LocatorsOrderingPage.phone_input).send_keys(Data.phone)

        self.driver.find_element(*LocatorsOrderingPage.metro_input).send_keys(metro_data)

        self.driver.find_element(*LocatorsOrderingPage.select_metro_station).click()

        self.driver.find_element(*LocatorsOrderingPage.next_button).click()

        self.driver.find_element(*LocatorsOrderingPage.data_input).click()

        self.driver.find_element(*date).click()

        self.driver.find_element(*LocatorsOrderingPage.dropdown_rent).click()

        self.driver.find_element(*rent).click()

        self.driver.find_element(*color).click()

        self.driver.find_element(*LocatorsOrderingPage.ordering_button).click()

        BasePage(self.driver).wait_need_element(LocatorsOrderingPage.yes_button)

        self.driver.find_element(*LocatorsOrderingPage.yes_button).click()

    @allure.step("Получение текста об успешном оформлении")
    def get_text_order(self):
        return self.driver.find_element(*LocatorsOrderingPage.status_field).text
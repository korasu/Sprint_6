import allure
from locators.locators_for_ordering_page import LocatorsOrderingPage
from base_page import BasePage
from data import Data

class OrderingPage(BasePage):
    def set_name(self):
        self.driver.find_element(*LocatorsOrderingPage.name_input).send_keys(Data.name)

    def set_second_name(self):
        self.driver.find_element(*LocatorsOrderingPage.second_name_input).send_keys(Data.second_name)

    def set_address(self):
        self.driver.find_element(*LocatorsOrderingPage.address_input).send_keys(Data.address)

    def set_number(self):
        self.driver.find_element(*LocatorsOrderingPage.phone_input).send_keys(Data.phone)

    def set_metro(self, metro_data):
        self.driver.find_element(*LocatorsOrderingPage.metro_input).send_keys(metro_data)

    def click_next_button(self):
        self.driver.find_element(*LocatorsOrderingPage.next_button).click()

    def set_date(self, date):
        self.driver.find_element(*date).click()

    def set_rent(self, rent):
        self.driver.find_element(*rent).click()

    def set_color(self, color):
        self.driver.find_element(*color).click()

    def click_order(self):
        self.driver.find_element(*LocatorsOrderingPage.ordering_button).click()

    def click_yes(self):
        self.driver.find_element(*LocatorsOrderingPage.yes_button).click()

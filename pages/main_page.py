import allure
from locators.locators_for_base_page import LocatorsBasePage
from pages.base_page import BasePage


class MainPage(BasePage):
    def click_yandex_logo(self):
        return self.driver.find_element(*LocatorsBasePage.yandex_logo).click()

    def click_scooter_logo(self):
        return self.driver.find_element(*LocatorsBasePage.scooter_logo).click()

    def click_header_ordering_button(self):
        self.driver.find_element(*LocatorsBasePage.header_order_button).click()

    def click_bottom_ordering_button(self):
        self.driver.find_element(*LocatorsBasePage.bottom_order_button).click()

    def scroll_to_question(self):
        element = self.driver.find_element(*LocatorsBasePage.eighth_question)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def click_on_question(self, question):
        self.driver.find_element(*question).click()
        self.wait_need_element(question, 3)

    def taken_answer(self, answer):
        return self.driver.find_element(*answer).text

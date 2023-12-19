import allure
from locators.locators_for_base_page import LocatorsBasePage
from pages.base_page import BasePage


class MainPage(BasePage):
    @allure.step('Нажать на лого "Яндекса"')
    def click_yandex_logo(self):
        return self.driver.find_element(*LocatorsBasePage.yandex_logo).click()

    @allure.step('Нажать на лого "Самоката"')
    def click_scooter_logo(self):
        return self.driver.find_element(*LocatorsBasePage.scooter_logo).click()

    @allure.step('Нажать на кнопку "заказать" в начале страницы')
    def click_header_ordering_button(self):
        self.driver.find_element(*LocatorsBasePage.header_order_button).click()

    @allure.step('Нажать на кнопку "заказать" в конце страницы')
    def click_bottom_ordering_button(self):
        self.driver.find_element(*LocatorsBasePage.bottom_order_button).click()

    @allure.step('Прокрутить страницу к блоку "Вопросы о главном"')
    def scroll_to_question(self):
        element = self.driver.find_element(*LocatorsBasePage.eighth_question)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Нажать на вопрос')
    def click_on_question(self, question):
        self.driver.find_element(*question).click()
        self.wait_need_element(question, 3)

    @allure.step('Получить текст ответа')
    def taken_answer(self, answer):
        return self.driver.find_element(*answer).text

import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.locators_for_base_page import LocatorsBasePage


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Открытие сайта")
    def open_site(self):
        return self.driver.get("https://qa-scooter.praktikum-services.ru")

    def wait_need_element(self, locator, time=5):
        return WebDriverWait(self.driver, time).until(expected_conditions.visibility_of_element_located(locator))

    @allure.step("Нажатие на кнопку Cookie")
    def click_cookie_button(self):
        self.driver.find_element(*LocatorsBasePage.cookie_button).click()

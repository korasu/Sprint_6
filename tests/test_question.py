import allure
import pytest

from pages.main_page import MainPage
from pages.base_page import BasePage
from locators.locators_for_base_page import LocatorsBasePage
from data import Data


class TestQuestion:
    question_and_answer = [
        [LocatorsBasePage.first_question, LocatorsBasePage.first_answer, Data.answer1],
        [LocatorsBasePage.second_question, LocatorsBasePage.second_answer, Data.answer2],
        [LocatorsBasePage.third_question, LocatorsBasePage.third_answer, Data.answer3],
        [LocatorsBasePage.fourth_question, LocatorsBasePage.fourth_answer, Data.answer4],
        [LocatorsBasePage.fifth_question, LocatorsBasePage.fifth_answer, Data.answer5],
        [LocatorsBasePage.six_question, LocatorsBasePage.six_answer, Data.answer6],
        [LocatorsBasePage.seventh_question, LocatorsBasePage.seventh_answer, Data.answer7],
        [LocatorsBasePage.eighth_question, LocatorsBasePage.eighth_answer, Data.answer8]
    ]

    @allure.title("Тест проверки блока 'Вопросы о главном'")
    @pytest.mark.parametrize('locator_question,locator_answer,answer', question_and_answer)
    def test_open_answer_on_question(self, driver, locator_question, locator_answer, answer):
        main_page = MainPage(driver)

        main_page.open_site()
        main_page.scroll_to_question()
        main_page.click_on_question(locator_question)
        actual_answer = main_page.taken_answer(locator_answer)

        assert actual_answer == answer

import allure
import pytest

from pages.main_page import MainPage
from locators.locators_for_base_page import LocatorsBasePage
from data import Answer


class TestQuestion:
    question_and_answer = [
        [LocatorsBasePage.first_question, LocatorsBasePage.first_answer, Answer.answer1],
        [LocatorsBasePage.second_question, LocatorsBasePage.second_answer, Answer.answer2],
        [LocatorsBasePage.third_question, LocatorsBasePage.third_answer, Answer.answer3],
        [LocatorsBasePage.fourth_question, LocatorsBasePage.fourth_answer, Answer.answer4],
        [LocatorsBasePage.fifth_question, LocatorsBasePage.fifth_answer, Answer.answer5],
        [LocatorsBasePage.six_question, LocatorsBasePage.six_answer, Answer.answer6],
        [LocatorsBasePage.seventh_question, LocatorsBasePage.seventh_answer, Answer.answer7],
        [LocatorsBasePage.eighth_question, LocatorsBasePage.eighth_answer, Answer.answer8]
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

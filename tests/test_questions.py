import allure
import pytest

import locators.locators as loc
from pages.main_page import MainPage
import data.urls as urls
import data.questins_data as que

class TesteQuestions:

    @allure.title('Проверка вопросов')
    @allure.description('Проверка вопросов о важном'
                        ' и проверяем ответы {que_data}')
    @pytest.mark.parametrize('que_data', [que.QUESTION_1,
                                          que.QUESTION_2,
                                          que.QUESTION_3,
                                          que.QUESTION_4,
                                          que.QUESTION_5,
                                          que.QUESTION_6,
                                          que.QUESTION_7,
                                          que.QUESTION_8])
    def test_questions_about_important_things(self, driver, que_data):

        driver = driver
        main_page = MainPage(driver, urls.MAIN_PAGE)
        # Открытие главной страницы
        main_page.open_main_page()
        # Принять куки
        main_page.accept_cookie()
        main_page.element_is_visible(loc.LOGO_BUTTON)
        #Прокрутка до вопросов
        main_page.scroll_to_questions()
        #Развернуть  вопрос
        main_page.expand_question(que_data)
        #Проверить ответ
        main_page.check_question(que_data)

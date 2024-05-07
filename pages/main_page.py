import allure
from selenium.webdriver.common.by import By

import locators.locators as loc
from pages.base_page import BasePage
from data import urls

class MainPage(BasePage):

    @allure.step("Открытие главной страницы")
    def open_main_page(self):

        self.open()

    @allure.step('Нажатие на верхнюю кнопку заказа')
    def click_upper_order_button(self):
        self.element_is_visible(loc.UPPER_ORDER_BUTTON).click()

    @allure.step('Нажатие на нижнюю кнопку заказа')
    def click_footer_order_button(self):

        self.scroll_to_element(loc.FOOTER_ORDER_BUTTON)
        self.element_is_visible(loc.FOOTER_ORDER_BUTTON).click()

    @allure.step('Нажатие на нижнюю кнопку заказа')
    def click_logo(self):

        self.element_is_visible(loc.SCOOTER_BUTTON).click()
        self.element_is_visible(loc.HOME_PAGE)

    @allure.step('Проверка перехода на главную страницу')
    def assert_to_main_page(self):

        url = self.get_url()
        assert url == urls.MAIN_PAGE

    @allure.step('Принять куки')
    def accept_cookie(self):

        self.element_is_visible(loc.COOKIE_BUTTON).click()

    @allure.step('Нажатие на логотип Яндекса')
    def click_dzen(self):

        self.element_is_visible(loc.LOGO_BUTTON).click()

    @allure.step('Проверка открытия новой вкладыки с Дзеном')
    def check_to_dzen_page(self):

        self.driver.switch_to.window(self.driver.window_handles[1])

    @allure.step('Прокрутка до вопросов')
    def scroll_to_questions(self):

        self.scroll_to_element(loc.QUESTIONS)

    @allure.step('Развернуть вопрос')
    def expand_question(self, data):

        element = self.element_is_visible(loc.index_que(data))
        element.click()

    @allure.step('Проверка ответа')
    def check_question(self, data):

        self.element_is_visible(loc.check_answer(data))

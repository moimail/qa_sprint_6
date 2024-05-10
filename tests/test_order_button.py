import allure
import pytest
import locators.locators as loc
from pages.main_page import MainPage
from pages.order_page import OrderPage
import data.urls as urls
import data.user_data as user_data

class TestOrderButton:

    @allure.title('Проверка заполнения данных пользователя через верхнюю кнопку заказа на странице оформления заказа')
    @allure.description('Заполняем форму "Для кого самокат" на странице оформления заказа'
                        ' и проверяем введенные данные: {user_info}')
    @pytest.mark.parametrize('user_info', [user_data.USER_1, user_data.USER_2])
    def test_order_upper_button(self, driver, user_info):

        main_page = MainPage(driver, urls.MAIN_PAGE)
        order_page = OrderPage(driver, urls.MAIN_PAGE)
        #Открытие главной страницы
        main_page.open_main_page()
        main_page.element_is_visible(loc.LOGO_BUTTON)
        # Принять куки
        main_page.accept_cookie()
        #Переход через верхнуюю кнопку заказа
        main_page.click_upper_order_button()
        #Заполнение данных пользователя
        order_page.fill_user_data(user_info)
        #Проверка вннесенных данных
        order_page.assert_user_data(user_info)
        #Переход в следующее меню
        order_page.click_next_button()
        #Заполнение информации о заказе
        order_page.fill_about_rent(user_info)
        #Проверка заполнения информации о заказе
        order_page.assert_about_rent(user_info)
        #Нажатие на кнопку заказа
        order_page.click_order_button()
        #Смотрим статус заказа
        order_page.order_info()

    @allure.title('Проверка заполнения данных пользователя через нижнюю кнопку заказа на странице оформления заказа')
    @allure.description('Заполняем форму "Для кого самокат" на странице оформления заказа'
                        ' и проверяем введенные данные: {user_info}')
    @pytest.mark.parametrize('user_info', [user_data.USER_1, user_data.USER_2])
    def test_order_footer_button(self, driver, user_info):

        main_page = MainPage(driver, urls.MAIN_PAGE)
        order_page = OrderPage(driver, urls.MAIN_PAGE)
        #Открытие главной страницы
        main_page.open_main_page()
        main_page.element_is_visible(loc.LOGO_BUTTON)
        # Принять куки
        main_page.accept_cookie()
        #Переход через нижнюю кнопку "Заказать"
        main_page.click_footer_order_button()
        # Заполнение данных пользователя
        order_page.fill_user_data(user_info)
        # Проверка вннесенных данных
        order_page.assert_user_data(user_info)
        # Переход в следующее меню
        order_page.click_next_button()
        # Заполнение информации о заказе
        order_page.fill_about_rent(user_info)
        # Проверка заполнения информации о заказе
        order_page.assert_about_rent(user_info)
        # Нажатие на кнопку заказа
        order_page.click_order_button()
        # Смотрим статус заказа
        order_page.order_info()





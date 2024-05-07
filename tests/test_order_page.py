import allure
import locators.locators as loc
from pages.main_page import MainPage
import data.urls as urls


class TestOrderPage:

    @allure.title('Проверка перехода на главную страницу при нажатии на логотип ')
    def test_logo_to_main(self, driver):

        main_page = MainPage(driver, urls.MAIN_PAGE)
        # Открытие главной страницы
        main_page.open_main_page()
        # Принять куки
        main_page.accept_cookie()
        main_page.element_is_visible(loc.LOGO_BUTTON)
        # Переход через верхнуюю кнопку заказа
        main_page.click_upper_order_button()
        #Нажатие на лого
        main_page.click_logo()
        #Проверка перехода на главную страницу
        main_page.assert_to_main_page()

    @allure.title('Проверка перехода на страницу Дзена')
    def test_go_to_dzen(self, driver):

        main_page = MainPage(driver, urls.MAIN_PAGE)
        # Открытие главной страницы
        main_page.open_main_page()
        # Принять куки
        main_page.accept_cookie()
        main_page.element_is_visible(loc.LOGO_BUTTON)
        #Переход через по лого Яндекс
        main_page.click_dzen()
        #Проверка перехода на странизу дзена
        main_page.check_to_dzen_page()




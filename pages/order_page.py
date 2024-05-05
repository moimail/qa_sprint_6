from datetime import  datetime
import allure
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from data import urls
from locators import locators


class OrderPage(BasePage):

    @allure.step("Открытие страницы заказов")
    def open_order_page(self):

        self.open(urls.ORDER_PAGE)

    @allure.step("Заполние данных пользователя {user_data}")
    def fill_user_data(self, user_data):

        #Заполнение имени
        element = self.element_is_visible(locators.NAME_FIELD)
        element.send_keys(user_data["first_name"])
        #Заполнение фамилии
        element = self.element_is_visible(locators.LAST_NAME_FIELD)
        element.send_keys(user_data["last_name"])
        #Заполнение адреса
        element = self.element_is_visible(locators.ADRESS_FIELS)
        element.send_keys(user_data["address"])
        #Выбор станции метро
        element = self.element_is_visible(locators.METRO_FIELD)
        element.click()
        element.send_keys(user_data["station"])
        element = self.element_is_visible(locators.SELECTED_METRO_STATION)
        element.click()
        #Ввод телефона
        element = self.element_is_visible(locators.PHONE_FIELD)
        element.send_keys(user_data["tel_number"])

    @allure.step("Проверка данных пользователя {user_data}")
    def assert_user_data(self, user_data):

        #Проверка имени
        element = self.element_is_visible(locators.NAME_FIELD)
        assert element.get_attribute("value") == user_data["first_name"]
        #Проверка фамилии
        element = self.element_is_visible(locators.LAST_NAME_FIELD)
        assert element.get_attribute("value") == user_data["last_name"]
        #Проверка адреса
        element = self.element_is_visible(locators.ADRESS_FIELS)
        assert element.get_attribute("value") == user_data["address"]
        #Проверка адреса
        element = self.element_is_visible(locators.ADRESS_FIELS)
        assert element.get_attribute("value") == user_data["address"]
        #Проверка станции метро
        element = self.element_is_visible(locators.METRO_FIELD)
        assert element.get_attribute("value") == user_data["station"]
        #Проверка телефона
        element = self.element_is_visible(locators.PHONE_FIELD)
        assert element.get_attribute("value") == user_data["tel_number"]

    @allure.step("Нажатие на кнопку далее")
    def click_next_button(self):
        # Нажатие на кнопку далее
        element = self.element_is_visible(locators.NEXT_BUTTON)
        element.click()

    @allure.step("Заполнение данных о заказе")
    def fill_about_rent(self, user_data):

        #Заполнение даты (заполняем текущим числом)
        element = self.element_is_visible(locators.DATE_FIELD)
        today = datetime.today()
        today = today.strftime("%d.%m.%Y")
        element.send_keys(today)
        element.send_keys(Keys.ENTER)
        #Заполняем срок аренды
        element = self.element_is_visible(locators.RENTAL_PERIOD_FIELD)
        element.click()
        element = self.element_is_visible([By.XPATH, f".//*[text()='{user_data["period"]}']"])
        element.click()
        #Выбор цвета
        element = self.element_is_visible([By.XPATH, f".//*[text()='{user_data["color"]}']"])
        element.click()
        #Запонение комментария
        element = self.element_is_visible(locators.COMMENT_FIELD)
        element.send_keys("_Тест")

    @allure.step("Проверка данных о заказе")
    def assert_about_rent(self, user_data):

        # проверка даты
        element = self.element_is_visible(locators.DATE_FIELD)
        today = datetime.today()
        assert element.get_attribute("value") ==  today.strftime("%d.%m.%Y")
        #Проверка комментария
        element = self.element_is_visible(locators.COMMENT_FIELD)
        assert element.get_attribute("value") == "_Тест"

    @allure.step("Подтверждение заказа")
    def click_order_button(self):

        #Нажатие кнопки "Заказать"
        element = self.element_is_visible(locators.ORDER_BUTTON)
        element.click()
        #Согласится  заказать
        element = self.element_is_visible(locators.CONFIRM_ORDER_BUTTON)
        element.click()

    @allure.step("Страница со статусом заказа")
    def order_info(self):

        #Перейти к заказу
        element = self.element_is_visible(locators.YES_BUTTON)
        element.click()
        element = self.element_is_visible(locators.SEE_STATUS_BUTTON)
        element.click()
        self.element_is_visible(locators.STATUS_ORDER_PAGE)







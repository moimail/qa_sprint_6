import time

import allure
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC, expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

import data.urls as urls


from conftest import driver

class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)

    @allure.step('Ожидание доступновсти элемента {locator}')
    def element_is_visible(self, locator, timeout=10):
        return Wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))




    @allure.step('Прокручиваем страницу до элемента по локатору {locator}')
    def scroll_to_element(self, locator):

        #Прокручиваем страницу до элемента по локатору
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Получить текущую URL')
    def get_url(self):

        return self.driver.current_url

    @allure.step('Проверка открытия новой вкладыки с Дзеном')
    def check_to_dzen_page(self):

        # Переключаемся на новую вкладку
        self.driver.switch_to.window(self.driver.window_handles[1])

        # Ждем изменения URL
        WebDriverWait(self.driver, 15).until(
            expected_conditions.url_changes(urls.BLANK))
        WebDriverWait(self.driver, 15).until(
            expected_conditions.url_to_be(urls.DZEN))

        # Проверяем URL
        url = self.driver.current_url
        assert url == urls.DZEN
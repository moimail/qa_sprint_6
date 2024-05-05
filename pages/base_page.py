import allure
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC


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
from selenium import webdriver
import allure
import pytest


@allure.step('Открываем браузер Firefox')
@pytest.fixture()
def driver():
    # создали драйвер для браузера Firefox
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    # закрываем драйвер после использования
    driver.quit()


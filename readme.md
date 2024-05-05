qa_python_6
Тест-сьют для проверки UI приложения "Самокат" с помощью Selenium и Pytest


Для запуска тестов должны быть установлены пакеты:

pytest,
selenium,
allure-pytest и
allure-python-commons.
Для генерации отчетов необходимо дополнительно установить:

    фреймворк Allure,
    JDK

Запуск всех тестов выполняется командой:

    pytest -v ./tests

Запуск тестов с генерацией отчета Allure выполняется командой:

    pytest -v ./tests  --alluredir=allure_results
Генерация отчета выполняется командой:


    allure serve allure_results
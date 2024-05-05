from selenium.webdriver.common.by import By

# Хедер
SCOOTER_BUTTON = [By.XPATH, ".//div[1]/a[2][@class='Header_LogoScooter__3lsAR']"]
LOGO_BUTTON = [By.XPATH, ".//a[@href='//yandex.ru']"]
HOME_PAGE = [By.XPATH, ".//div[4][@class = 'Home_Header__iJKdX']"]

#Хедер Дзена
HEADER_DZEN = [By.XPATH, ".//div[3][@class = 'y5Iohvhmb5d2CQby8__yandexSearchContainer-2y']"]  #Закгловок Дзена

#Верхняя кнопка заказа

UPPER_ORDER_BUTTON = [By.XPATH, "(.//button[text()='Заказать'])[1]"]  #Верхняя кнопка заказа
FOOTER_ORDER_BUTTON = [By.XPATH, "(.//button[text()='Заказать'])[2]"] #Нижняя кнопка заказа

#Данные о заказе
NAME_FIELD = [By.XPATH, ".//input[@placeholder = '* Имя']"]  #Поле ввода имени
LAST_NAME_FIELD = [By.XPATH, ".//input[@placeholder = '* Фамилия']"]  #Поле ввода фамилии
ADRESS_FIELS = [By.XPATH, ".//input[@placeholder = '* Адрес: куда привезти заказ']"] #Поле ввода адреса
METRO_FIELD = [By.XPATH, ".//input[@placeholder = '* Станция метро']"] #Поле ввода метро
PHONE_FIELD = [By.XPATH, ".//input[@placeholder = '* Телефон: на него позвонит курьер']"] #Поле ввода телефона
NEXT_BUTTON = [By.XPATH, ".//button[text() = 'Далее']"] #Кнопка "Далее"
COOKIE_BUTTON = [By.XPATH, ".//button[@class = 'App_CookieButton__3cvqF']"] #Кнопка "Куки"
DATE_FIELD = [By.XPATH, ".//input[@placeholder = '* Когда привезти самокат']"] #Поле даты заказа
RENTAL_PERIOD_FIELD = [By.XPATH, ".//div[@class = 'Dropdown-control']"] #Поле срока аренды
RENTAL_PERIOD_FIELD_SELECTED = [By.XPATH, ".//div[@class = 'Dropdown-placeholder is-selected']"] #Поле срока аренды
CHOICE_COLOR = [By.XPATH, ".//label[1]/input[@class = 'Checkbox_Input__14A2w']"] #Поле выбра цвета
COMMENT_FIELD = [By.XPATH, ".//input[@placeholder = 'Комментарий для курьера']"] #Поле ввода комментария
ORDER_BUTTON = [By.XPATH, ".//button[2][text() = 'Заказать']"] #Кнопка "Заказат"
CONFIRM_ORDER_BUTTON = [By.XPATH, ".//div[@class = 'Order_Modal__YZ-d3']"] #
YES_BUTTON = [By.XPATH, ".//button[2][text() = 'Да']"] # Кнопка "Да"
NO_BUTTON = [By.XPATH, ".//button[1][text() = 'Нет']"] #Кнопка "Нет"
ORDER_COMPLETE_FORM = [By.XPATH, ".//div[1][text() = 'Заказ оформлен']"] #Завершение заказа
SEE_STATUS_BUTTON = [By.XPATH, ".//button[text() = 'Посмотреть статус']"] #Кнопка просмотра статуса
STATUS_ORDER_PAGE = [By.XPATH, ".//div[1]/div/input[@class = 'Input_Input__1iN_Z Track_Input__1g7lq Input_Filled__1rDxs Input_Responsible__1jDKN']"] # Страница статуса
SELECTED_METRO_STATION = [By.CLASS_NAME, 'select-search__select'] #Выбор станции метро

#Вопросы
QUESTIONS = [By.XPATH, f"//*[@id ='accordion__heading-0']"]
from selenium.webdriver.common.by import By


class LocatorsOrderingPage:
    # поле ввода имени
    name_input = (By.XPATH, './/input[@placeholder = "* Имя"]')
    # поле ввода Фамилии
    second_name_input = (By.XPATH, './/input[@placeholder = "* Фамилия"]')
    # поле ввода Адреса
    address_input = (By.XPATH, './/input[@placeholder = "* Адрес: куда привезти заказ"]')
    # поле ввода метро
    metro_input = (By.XPATH, './/input[@placeholder = "* Станция метро"]')
    # выбор станции из списка
    select_metro_station = (By.CLASS_NAME, "select-search__select")
    # поле ввода телефона
    phone_input = (By.XPATH, './/input[@placeholder = "* Телефон: на него позвонит курьер"]')
    # поле ввода даты
    data_input = (By.XPATH, './/input[@placeholder = "* Когда привезти самокат"]')
    # дата для первого теста
    first_data = (By.XPATH, ".//div[@aria-label = 'Choose вторник, 19-е декабря 2023 г.']")
    # дата для второго теста
    second_data = (By.XPATH, ".//div[@aria-label = 'Choose четверг, 7-е декабря 2023 г.']")
    dropdown_rent = (By.XPATH, ".//span[@class = 'Dropdown-arrow']")
    # срок аренды для первого теста
    first_rent_time = (By.XPATH, ".//div[@class = 'Dropdown-option' and text() = 'трое суток']")
    # срок аренды для второго теста
    second_rent_time = (By.XPATH, ".//div[@class = 'Dropdown-option' and text() = 'пятеро суток']")
    # цвет самоката для первого теста
    black_scooter = (By.ID, "black")
    # цвет самоката для второго теста
    grey_scooter = (By.ID, "grey")
    # поле ввода комментария
    comment_input = (By.XPATH, './/input[@placeholder = "Комментарий для курьера"]')
    # кнопка для продолжения оформления
    next_button = (By.XPATH, './/button[text() = "Далее"]')
    # кнопка для заказа
    ordering_button = (By.XPATH, './/div[@class = "Order_Buttons__1xGrp"]/button[text() = "Заказать"]')
    # кнопка для подтверждения заказа
    yes_button = (By.XPATH, './/button[text() = "Да"]')
    # кнопка для отказа от заказа
    no_button = (By.XPATH, './/button[text() = "Нет"]')
    # поле статуса заказа
    status_field = (By.XPATH, './/div[@class = "Order_ModalHeader__3FDaJ"]')


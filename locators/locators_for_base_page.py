from selenium.webdriver.common.by import By


class LocatorsBasePage:
    # логотип яндекса
    yandex_logo = (By.CLASS_NAME, 'Header_LogoYandex__3TSOI')
    # логотип самоката
    scooter_logo = (By.CLASS_NAME, 'Header_LogoScooter__3lsAR')
    # кнопка для принятия кук
    cookie_button = (By.ID, 'rcc-confirm-button')
    # кнопка для оформления заказа в начале страницы
    header_order_button = (By.CLASS_NAME, 'Button_Button__ra12g')
    # кнопка для оформления заказа в конце страницы
    bottom_order_button = (By.XPATH, './/div[@class = "Home_FinishButton__1_cWm"]/button[text() = "Заказать"]')
    # кнопки вопросов
    first_question = (By.ID, "accordion__heading-0")
    second_question = (By.ID, "accordion__heading-1")
    third_question = (By.ID, "accordion__heading-2")
    fourth_question = (By.ID, "accordion__heading-3")
    fifth_question = (By.ID, "accordion__heading-4")
    six_question = (By.ID, "accordion__heading-5")
    seventh_question = (By.ID, "accordion__heading-6")
    eighth_question = (By.ID, "accordion__heading-7")
    # ответы на вопросы
    first_answer = (By.ID, "accordion__panel-0")
    second_answer = (By.ID, "accordion__panel-1")
    third_answer = (By.ID, "accordion__panel-2")
    fourth_answer = (By.ID, "accordion__panel-3")
    fifth_answer = (By.ID, "accordion__panel-4")
    six_answer = (By.ID, "accordion__panel-5")
    seventh_answer = (By.ID, "accordion__panel-6")
    eighth_answer = (By.ID, "accordion__panel-7")
    # банер с предложение установки Яндекс браузера на странице Дзена
    banner_yandex_browser = (By.XPATH, ".//div[@popup-getfocusable-id = 'csr-uniq3']")

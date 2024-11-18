from selenium.webdriver.common.by import By


class TestLocators:
    LOGIN_MAIN_PAGE = [By.XPATH, "//button[contains(@class, 'button_button_type_primary') and text()='Войти в аккаунт']"]  # кнопка "Войти в аккаунт" на главной
    LOGIN_PERSONAL_ACCOUNT = [By.XPATH, "//p[contains(@class, 'AppHeader_header') and text()='Личный Кабинет']"] # кнопка "Личный кабинет" на главной
    LOGIN_IN_REGISTRATION_FORM = [By.XPATH, "//a[contains(@class , 'Auth_link') and text() = 'Войти']"] # кнопка "Войти" в форме регистрации
    LOGIN_IN_PASSWORD_PASSWORD_RECOVERY_FORM = [By.XPATH, "//a[contains(@class , 'Auth_link') and text() = 'Войти']"] # кнопка "Войти" в форме восстановления пароля
    LOGIN_FINISH_BUTTON = [By.XPATH, "//button[contains(@class, 'button_button_type_primary') and text()='Войти']"] # кнопка "Войти" в форме авторизации (при вводе Email и Пароль)

    LOGOUT_BUTTON = [By.XPATH, "//button[@type='button' and text()='Выход']"] # кнопка "Выйти"

    REGISTRATION_START_BUTTON = [By.XPATH, "//a[@href='/register' and text()='Зарегистрироваться']"] # кнопка "Зарегистрироваться" в разделе авторизации (для открытия формы регистрации)
    REGISTRATION_FINISH_BUTTON = [By.XPATH, "//button[text()='Зарегистрироваться']"] # кнопка "Зарегистрироваться" в форме регистрации

    NAME_INPUT_FIELD_REGISTRATION = [By.XPATH, "//label[text()='Имя']/following-sibling::input"] # поле ввода Имя в регистрации
    EMAIL_INPUT_FIELD_REGISTRATION = [By.XPATH, "//label[text()='Email']/following-sibling::input"] # поле ввода email в регистрации
    PASSWORD_INPUT_FIELD_REGISTRATION = [By.XPATH, "//input[@type='password' and @name='Пароль']"] # поле вода пароля в регистрации

    EMAIL_INPUT_FIELD_AUTHORIZATION = [By.XPATH, "//label[text()='Email']/following-sibling::input"] # поле ввода email в авторизации
    PASSWORD_INPUT_FIELD_AUTHORIZATION = [By.XPATH, "//input[@type='password' and @name='Пароль']"] # поле ввода email в авторизации

    PLACE_ORDER_BUTTON = [By.XPATH, "//*[text()='Оформить заказ']"] # кнопка "Оформить заказ" у авторизованного пользователя

    PASSWORD_RECOVERY_BUTTON = [By.XPATH, "//a[text()='Восстановить пароль']"] # "Восстановить пароль" в форме авторизации

    CONSTRUCTOR_BUTTON = [By.XPATH, "//p[contains(@class, 'AppHeader_header') and text()='Конструктор']"] # "Конструктор" в хэдере
    CONSTRUCTOR_GENERAL_FORM = [By.XPATH, "//h1[contains(@class, 'text_type_main-large') and text()='Соберите бургер']"] # Общая/главная страница Конструктора с информингом "Соберите бургер"

    STELLAR_BURGERS_BUTTON = [By.XPATH, "//a/*[name()='svg']"] # логотип Stellar Burgers

    SAUCES_IN_CONSTRUCTOR = [By.XPATH, "//*[@class='text text_type_main-default' and text()='Соусы']"] # раздел Соусы в конструкторе
    SAUCES_HEADER_SECTION = [By.XPATH, "//*[@class='text text_type_main-medium mb-6 mt-10' and text()='Соусы']"] # Хэдер секции Соусы в конструкторе
    BUNS_IN_CONSTRUCTOR = [By.XPATH, "//*[@class='text text_type_main-default' and text()='Булки']"] # раздел Булки в конструкторе
    BUNS_HEADER_SECTION = [By.XPATH, "//*[@class='text text_type_main-medium mb-6 mt-10' and text()='Булки']"] # Хэдер секции Соусы в конструкторе
    FILLINGS_IN_CONSTRUCTOR = [By.XPATH, "//*[@class='text text_type_main-default' and text()='Начинки']"]  # раздел Начинки в конструкторе
    FILLINGS_HEADER_SECTION = [By.XPATH,"//*[@class='text text_type_main-medium mb-6 mt-10' and text()='Начинки']"]  # Хэдер секции Соусы в конструкторе
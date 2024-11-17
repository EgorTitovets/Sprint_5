from selenium.webdriver.common.by import By


class TestLocators:
    LOGIN_MAIN_PAGE = [By.XPATH, "/html/body/div[1]/div/main/section[2]/div/button"]  # кнопка "Войти в аккаунт" на главной
    LOGIN_PERSONAL_ACCOUNT = [By.XPATH, "/html/body/div[1]/div/header/nav/a"] # кнопка "Личный кабинет" на главной
    LOGIN_IN_REGISTRATION_FORM = [By.XPATH, "/html/body/div[1]/div/main/div/div/p/a"] # кнопка "Войти" в форме регистрации
    LOGIN_IN_PASSWORD_PASSWORD_RECOVERY_FORM = [By.XPATH, "/html/body/div[1]/div/main/div/div/p/a"] # кнопка "Войти" в форме восстановления пароля
    LOGIN_FINISH_BUTTON = [By.XPATH, "/html/body/div[1]/div/main/div/form/button"] # кнопка "Войти" в форме авторизации (при вводе Email и Пароль)

    LOGOUT_BUTTON = [By.XPATH, "/html/body/div[1]/div/main/div/nav/ul/li[3]/button"] # кнопка "Выйти"

    REGISTRATION_START_BUTTON = [By.XPATH, "/html/body/div[1]/div/main/div/div/p[1]/a"] # кнопка "Зарегистрироваться" в разделе авторизации (для открытия формы регистрации)
    REGISTRATION_FINISH_BUTTON = [By.XPATH, "/html/body/div[1]/div/main/div/form/button"] # кнопка "Зарегистрироваться" в форме регистрации

    NAME_INPUT_FIELD_REGISTRATION = [By.XPATH, "/html/body/div[1]/div/main/div/form/fieldset[1]/div/div/input"] # поле ввода Имя в регистрации
    EMAIL_INPUT_FIELD_REGISTRATION = [By.XPATH, "/html/body/div[1]/div/main/div/form/fieldset[2]/div/div/input"] # поле ввода email в регистрации
    PASSWORD_INPUT_FIELD_REGISTRATION = [By.XPATH, "/html/body/div[1]/div/main/div/form/fieldset[3]/div/div/input"] # поле вода пароля в регистрации

    EMAIL_INPUT_FIELD_AUTHORIZATION = [By.XPATH, '/html/body/div[1]/div/main/div/form/fieldset[1]/div/div/input'] # поле ввода email в авторизации
    PASSWORD_INPUT_FIELD_AUTHORIZATION = [By.XPATH, "/html/body/div[1]/div/main/div/form/fieldset[2]/div/div/input"] # поле ввода email в авторизации

    PLACE_ORDER_BUTTON = [By.XPATH, "/html/body/div[1]/div/main/section[2]/div/button"] # кнопка "Оформить заказ" у авторизованного пользователя

    PASSWORD_RECOVERY_BUTTON = [By.XPATH, "/html/body/div[1]/div/main/div/div/p[2]/a"] # "Восстановить пароль" в форме авторизации

    CONSTRUCTOR_BUTTON = [By.XPATH, "/html/body/div/div/header/nav/ul/li[1]/a/p"] # "Конструктор" в хэдере
    CONSTRUCTOR_GENERAL_FORM = [By.XPATH, "/html/body/div[1]/div/main/section[1]/h1"] # Общая/главная страница Конструктора с информингом "Соберите бургер"

    STELLAR_BURGERS_BUTTON = [By.XPATH, "//*[@id='root']/div/header/nav/div/a"] # логотип Stellar Burgers
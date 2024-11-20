from locators import TestLocators
from data import existing_user


class TestRedirectFromPersonalAccount:

    def test_redirect_to_constructor_by_click_constructor(self, driver):
        driver.find_element(*TestLocators.LOGIN_MAIN_PAGE).click()
        driver.find_element(*TestLocators.EMAIL_INPUT_FIELD_AUTHORIZATION).send_keys(existing_user['email'])
        driver.find_element(*TestLocators.PASSWORD_INPUT_FIELD_AUTHORIZATION).send_keys(existing_user['password'])
        driver.find_element(*TestLocators.LOGIN_FINISH_BUTTON).click()
        driver.find_element(*TestLocators.LOGIN_PERSONAL_ACCOUNT).click()
        driver.find_element(*TestLocators.CONSTRUCTOR_BUTTON).click()

        assert driver.find_element(*TestLocators.CONSTRUCTOR_GENERAL_FORM).text == "Соберите бургер"

    def test_redirect_to_constructor_by_click_stellar_burgers(self, driver):
        driver.find_element(*TestLocators.LOGIN_MAIN_PAGE).click()
        driver.find_element(*TestLocators.EMAIL_INPUT_FIELD_AUTHORIZATION).send_keys(existing_user['email'])
        driver.find_element(*TestLocators.PASSWORD_INPUT_FIELD_AUTHORIZATION).send_keys(existing_user['password'])
        driver.find_element(*TestLocators.LOGIN_FINISH_BUTTON).click()
        driver.find_element(*TestLocators.LOGIN_PERSONAL_ACCOUNT).click()
        driver.find_element(*TestLocators.STELLAR_BURGERS_BUTTON).click()

        assert driver.find_element(*TestLocators.CONSTRUCTOR_GENERAL_FORM).text == "Соберите бургер"

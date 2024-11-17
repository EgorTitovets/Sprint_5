from selenium.webdriver.common.by import By

from locators import TestLocators
from data import existing_user
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestLogin:

    def test_login_from_main_page_login_to_your_account_button(self, driver):
        driver.find_element(*TestLocators.LOGIN_MAIN_PAGE).click()
        driver.find_element(*TestLocators.EMAIL_INPUT_FIELD_AUTHORIZATION).send_keys(existing_user['email'])
        driver.find_element(*TestLocators.PASSWORD_INPUT_FIELD_AUTHORIZATION).send_keys(existing_user['password'])
        driver.find_element(*TestLocators.LOGIN_FINISH_BUTTON).click()

        WebDriverWait(driver, 10).until(
            expected_conditions.presence_of_element_located((By.XPATH, "//*[text()='Оформить заказ']")))

        assert driver.find_element(*TestLocators.PLACE_ORDER_BUTTON).text == "Оформить заказ"

    def test_login_from_personal_account_button(self, driver):
        driver.find_element(*TestLocators.LOGIN_PERSONAL_ACCOUNT).click()
        driver.find_element(*TestLocators.EMAIL_INPUT_FIELD_AUTHORIZATION).send_keys(existing_user['email'])
        driver.find_element(*TestLocators.PASSWORD_INPUT_FIELD_AUTHORIZATION).send_keys(existing_user['password'])
        driver.find_element(*TestLocators.LOGIN_FINISH_BUTTON).click()

        WebDriverWait(driver, 10).until(
            expected_conditions.presence_of_element_located((By.XPATH, "//*[text()='Оформить заказ']")))

        assert driver.find_element(*TestLocators.PLACE_ORDER_BUTTON).text == "Оформить заказ"

    def test_login_from_registration_form(self, driver):
        driver.find_element(*TestLocators.LOGIN_MAIN_PAGE).click()
        driver.find_element(*TestLocators.REGISTRATION_START_BUTTON).click()
        driver.find_element(*TestLocators.LOGIN_IN_REGISTRATION_FORM).click()
        driver.find_element(*TestLocators.EMAIL_INPUT_FIELD_AUTHORIZATION).send_keys(existing_user['email'])
        driver.find_element(*TestLocators.PASSWORD_INPUT_FIELD_AUTHORIZATION).send_keys(existing_user['password'])
        driver.find_element(*TestLocators.LOGIN_FINISH_BUTTON).click()

        WebDriverWait(driver, 10).until(
            expected_conditions.presence_of_element_located((By.XPATH, "//*[text()='Оформить заказ']")))

        assert driver.find_element(*TestLocators.PLACE_ORDER_BUTTON).text == "Оформить заказ"

    def test_login_from_password_recovery_form(self, driver):
        driver.find_element(*TestLocators.LOGIN_MAIN_PAGE).click()
        driver.find_element(*TestLocators.PASSWORD_RECOVERY_BUTTON).click()
        driver.find_element(*TestLocators.LOGIN_IN_PASSWORD_PASSWORD_RECOVERY_FORM).click()
        driver.find_element(*TestLocators.EMAIL_INPUT_FIELD_AUTHORIZATION).send_keys(existing_user['email'])
        driver.find_element(*TestLocators.PASSWORD_INPUT_FIELD_AUTHORIZATION).send_keys(existing_user['password'])
        driver.find_element(*TestLocators.LOGIN_FINISH_BUTTON).click()

        WebDriverWait(driver, 10).until(
            expected_conditions.presence_of_element_located((By.XPATH, "//*[text()='Оформить заказ']")))

        assert driver.find_element(*TestLocators.PLACE_ORDER_BUTTON).text == "Оформить заказ"

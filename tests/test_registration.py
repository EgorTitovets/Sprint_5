import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import TestLocators


class TestRegistration:

    def test_successful_registration(self, driver):
        driver.find_element(*TestLocators.LOGIN_MAIN_PAGE).click()
        driver.find_element(*TestLocators.REGISTRATION_START_BUTTON).click()
        driver.find_element(*TestLocators.NAME_INPUT_FIELD_REGISTRATION).send_keys('Pups')
        new_email = "egortitovets15" + str(random.randint(100, 999)) + "@ya.ru"
        driver.find_element(*TestLocators.EMAIL_INPUT_FIELD_REGISTRATION).send_keys(
            new_email)
        driver.find_element(*TestLocators.PASSWORD_INPUT_FIELD_REGISTRATION).send_keys(
            'pipipi')
        driver.find_element(*TestLocators.REGISTRATION_FINISH_BUTTON).click()

        WebDriverWait(driver, 10).until(
            expected_conditions.text_to_be_present_in_element(TestLocators.LOGIN_FINISH_BUTTON, "Войти"))

        assert driver.find_element(*TestLocators.LOGIN_FINISH_BUTTON).text == 'Войти'

    def test_invalid_password(self, driver):
        driver.find_element(*TestLocators.LOGIN_MAIN_PAGE).click()
        driver.find_element(*TestLocators.REGISTRATION_START_BUTTON).click()
        driver.find_element(*TestLocators.NAME_INPUT_FIELD_REGISTRATION).send_keys('Pups')
        new_email = "egortitovets15" + str(random.randint(100, 999)) + "@ya.ru"
        driver.find_element(*TestLocators.EMAIL_INPUT_FIELD_REGISTRATION).send_keys(
            new_email)
        driver.find_element(*TestLocators.PASSWORD_INPUT_FIELD_REGISTRATION).send_keys(
            'pipip')
        driver.find_element(*TestLocators.REGISTRATION_FINISH_BUTTON).click()

        error_message = WebDriverWait(driver, 3).until(
            expected_conditions.presence_of_element_located(TestLocators.INVALID_PASSWORD)).text

        WebDriverWait(driver, 10).until(
            expected_conditions.presence_of_element_located(TestLocators.INVALID_PASSWORD))

        assert 'Некорректный пароль' in error_message

from locators import TestLocators
from data import existing_user
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By


class TestLogout:

    def test_logout_by_button_click_in_personal_account(self, driver):
        driver.find_element(*TestLocators.LOGIN_MAIN_PAGE).click()
        driver.find_element(*TestLocators.EMAIL_INPUT_FIELD_AUTHORIZATION).send_keys(existing_user['email'])
        driver.find_element(*TestLocators.PASSWORD_INPUT_FIELD_AUTHORIZATION).send_keys(existing_user['password'])
        driver.find_element(*TestLocators.LOGIN_FINISH_BUTTON).click()
        driver.find_element(*TestLocators.LOGIN_PERSONAL_ACCOUNT).click()

        WebDriverWait(driver, 10).until(
            expected_conditions.presence_of_element_located((By.XPATH, "//*[text()='Выход']")))

        driver.find_element(*TestLocators.LOGOUT_BUTTON).click()

        WebDriverWait(driver, 10).until(
            expected_conditions.presence_of_element_located((By.XPATH, "//*[text()='Войти']")))

        assert driver.find_element(*TestLocators.LOGIN_FINISH_BUTTON).text == "Войти"

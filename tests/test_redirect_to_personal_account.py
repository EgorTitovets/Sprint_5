from locators import TestLocators
from data import existing_user
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestRedirectToPersonalAccount:

    def test_redirect_to_personal_account_by_click(self, driver):
        driver.find_element(*TestLocators.LOGIN_MAIN_PAGE).click()
        driver.find_element(*TestLocators.EMAIL_INPUT_FIELD_AUTHORIZATION).send_keys(existing_user['email'])
        driver.find_element(*TestLocators.PASSWORD_INPUT_FIELD_AUTHORIZATION).send_keys(existing_user['password'])
        driver.find_element(*TestLocators.LOGIN_FINISH_BUTTON).click()
        driver.find_element(*TestLocators.LOGIN_PERSONAL_ACCOUNT).click()

        WebDriverWait(driver, 5).until(expected_conditions.url_contains("/account/profile"))

        assert "/account/profile" in driver.current_url

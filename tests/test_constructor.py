from locators import TestLocators


class TestRedirectConstructor:

    def test_redirect_to_sauces_section(self, driver):
        sauces_section = driver.find_element(*TestLocators.SAUCES_IN_CONSTRUCTOR)
        sauces_section.click()
        driver.execute_script("arguments[0].scrollIntoView();", sauces_section)
        sauces_header = driver.find_element(*TestLocators.SAUCES_HEADER_SECTION)
        assert sauces_header.is_displayed()

    def test_redirect_to_buns_section(self, driver):
        driver.find_element(*TestLocators.SAUCES_IN_CONSTRUCTOR).click()
        buns_section = driver.find_element(*TestLocators.BUNS_IN_CONSTRUCTOR)
        buns_section.click()
        driver.execute_script("arguments[0].scrollIntoView();", buns_section)
        buns_header = driver.find_element(*TestLocators.SAUCES_HEADER_SECTION)
        assert buns_header.is_displayed()

    def test_redirect_to_fillings_section(self, driver):
        fillings_section = driver.find_element(*TestLocators.FILLINGS_IN_CONSTRUCTOR)
        fillings_section.click()
        driver.execute_script("arguments[0].scrollIntoView();", fillings_section)
        fillings_header = driver.find_element(*TestLocators.FILLINGS_HEADER_SECTION)
        assert fillings_header.is_displayed()

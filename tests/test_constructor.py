from selenium.webdriver.common.by import By


class TestRedirectConstructor:

    def test_redirect_to_sauces_section(self, driver):
        sauces_section = driver.find_element(By.XPATH, "/html/body/div[1]/div/main/section[1]/div[1]/div[2]/span")
        sauces_section.click()
        driver.execute_script("arguments[0].scrollIntoView();", sauces_section)
        sauces_header = driver.find_element(By.XPATH, "//*[text()='Соусы']")
        assert sauces_header.is_displayed()

    def test_redirect_to_buns_section(self, driver):
        driver.find_element(By.XPATH, "/html/body/div[1]/div/main/section[1]/div[1]/div[2]/span").click()
        buns_section = driver.find_element(By.XPATH, "/html/body/div[1]/div/main/section[1]/div[1]/div[1]/span")
        buns_section.click()
        driver.execute_script("arguments[0].scrollIntoView();", buns_section)
        buns_section = driver.find_element(By.XPATH, "//*[text()='Булки']")
        assert buns_section.is_displayed()

    def test_redirect_to_fillings_section(self, driver):
        fillings_section = driver.find_element(By.XPATH, "/html/body/div[1]/div/main/section[1]/div[1]/div[3]/span")
        fillings_section.click()
        driver.execute_script("arguments[0].scrollIntoView();", fillings_section)
        fillings_section = driver.find_element(By.XPATH, "//*[text()='Начинки']")
        assert fillings_section.is_displayed()

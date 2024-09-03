from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from src.config import Config, TestData
from src.locators import BurgerLocators

class TestExit:
    def test_exit_from_personal_account(self, driver):
        driver.get(Config.URL)
        driver.find_element(*BurgerLocators.LOGIN_TO_ACCOUNT_BUTTON).click()
        driver.find_element(*BurgerLocators.EMAIL_FIELD).send_keys(TestData.EMAIL)
        driver.find_element(*BurgerLocators.PASSWORD_FIELD).send_keys(TestData.PASSWORD)
        driver.find_element(*BurgerLocators.LOGIN_BUTTON).click()
        driver.find_element(*BurgerLocators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, Config.TIMEOUT).until(expected_conditions.visibility_of_element_located(BurgerLocators.ACCOUNT_LIST))
        driver.find_element(*BurgerLocators.LOGOUT_BUTTON).click()
        WebDriverWait(driver, Config.TIMEOUT).until(expected_conditions.visibility_of_element_located(BurgerLocators.LOGIN_BUTTON))
        assert driver.current_url == f'{Config.URL}/login'


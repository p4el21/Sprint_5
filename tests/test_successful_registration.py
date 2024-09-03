from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from conftest import generate_data
from src.config import Config, TestData
from src.locators import BurgerLocators

class TestRegistration:
    def test_successful_registration(self, driver, generate_data):
        driver.get(Config.URL)
        email, password = generate_data
        driver.find_element(*BurgerLocators.LOGIN_TO_ACCOUNT_BUTTON).click()
        driver.find_element(*BurgerLocators.REGISTRATION_LINK).click()
        driver.find_element(*BurgerLocators.NAME_FIELD).send_keys(TestData.NAME)
        driver.find_element(*BurgerLocators.EMAIL_FIELD).send_keys(email)
        driver.find_element(*BurgerLocators.PASSWORD_FIELD).send_keys(password)
        driver.find_element(*BurgerLocators.REGISTRATION_BUTTON).click()
        WebDriverWait(driver, Config.TIMEOUT).until(expected_conditions.visibility_of_element_located(BurgerLocators.LOGIN_BUTTON))
        driver.find_element(*BurgerLocators.EMAIL_FIELD).send_keys(email)
        driver.find_element(*BurgerLocators.PASSWORD_FIELD).send_keys(password)
        driver.find_element(*BurgerLocators.LOGIN_BUTTON).click()
        WebDriverWait(driver, Config.TIMEOUT).until(expected_conditions.visibility_of_element_located(BurgerLocators.ORDER_BUTTON))
        assert driver.current_url == f'{Config.URL}/'


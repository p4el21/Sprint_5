from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from src.config import Config
from src.locators import BurgerLocators

class TestSuccessfulLogin:
    def test_successfully_login_on_main(self, driver):
        driver.get(Config.URL)

        driver.find_element(*BurgerLocators.LOGIN_TO_ACCOUNT_BUTTON).click()

        driver.find_element(*BurgerLocators.EMAIL_FIELD).send_keys(Config.EMAIL)
        driver.find_element(*BurgerLocators.PASSWORD_FIELD).send_keys(Config.PASSWORD)
        driver.find_element(*BurgerLocators.LOGIN_BUTTON).click()

        WebDriverWait(driver, Config.TIMEOUT).until(expected_conditions.visibility_of_element_located(BurgerLocators.ORDER_BUTTON))

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'

    def test_successful_login_from_personal_account(self, driver):
        driver.get(Config.URL)

        driver.find_element(*BurgerLocators.PERSONAL_ACCOUNT_BUTTON).click()

        driver.find_element(*BurgerLocators.EMAIL_FIELD).send_keys(Config.EMAIL)
        driver.find_element(*BurgerLocators.PASSWORD_FIELD).send_keys(Config.PASSWORD)
        driver.find_element(*BurgerLocators.LOGIN_BUTTON).click()

        WebDriverWait(driver, Config.TIMEOUT).until(expected_conditions.visibility_of_element_located(BurgerLocators.ORDER_BUTTON))

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'

    def test_successful_login_from_registration_form(self, driver):
        driver.get(Config.URL)

        driver.find_element(*BurgerLocators.LOGIN_TO_ACCOUNT_BUTTON).click()
        driver.find_element(*BurgerLocators.REGISTRATION_LINK).click()

        driver.find_element(*BurgerLocators.LOGIN_LINK).click()

        driver.find_element(*BurgerLocators.EMAIL_FIELD).send_keys(Config.EMAIL)
        driver.find_element(*BurgerLocators.PASSWORD_FIELD).send_keys(Config.PASSWORD)
        driver.find_element(*BurgerLocators.LOGIN_BUTTON).click()

        WebDriverWait(driver, Config.TIMEOUT).until(expected_conditions.visibility_of_element_located(BurgerLocators.ORDER_BUTTON))

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'

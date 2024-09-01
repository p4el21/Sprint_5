from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from src.config import Config
from src.locators import BurgerLocators

class TestConstructor:
    def test_go_to_section_buns(self, driver):
        driver.get(Config.URL)

        driver.find_element(*BurgerLocators.LOGIN_TO_ACCOUNT_BUTTON).click()

        driver.find_element(*BurgerLocators.EMAIL_FIELD).send_keys(Config.EMAIL)
        driver.find_element(*BurgerLocators.PASSWORD_FIELD).send_keys(Config.PASSWORD)
        driver.find_element(*BurgerLocators.LOGIN_BUTTON).click()

        WebDriverWait(driver, Config.TIMEOUT).until(expected_conditions.visibility_of_element_located(BurgerLocators.ORDER_BUTTON))

        driver.find_element(*BurgerLocators.BUNS_TEXT)

        WebDriverWait(driver, Config.TIMEOUT).until(expected_conditions.visibility_of_element_located(BurgerLocators.ORDER_BUTTON))

        assert driver.find_element(*BurgerLocators.ACTIVE_LINE)

    def test_go_to_section_fillings(self, driver):
        driver.get(Config.URL)

        driver.find_element(*BurgerLocators.LOGIN_TO_ACCOUNT_BUTTON).click()

        driver.find_element(*BurgerLocators.EMAIL_FIELD).send_keys(Config.EMAIL)
        driver.find_element(*BurgerLocators.PASSWORD_FIELD).send_keys(Config.PASSWORD)
        driver.find_element(*BurgerLocators.LOGIN_BUTTON).click()

        WebDriverWait(driver, Config.TIMEOUT).until(expected_conditions.visibility_of_element_located(BurgerLocators.ORDER_BUTTON))

        driver.find_element(*BurgerLocators.FILLINGS_TEXT).click()

        WebDriverWait(driver, Config.TIMEOUT).until(expected_conditions.visibility_of_element_located(BurgerLocators.ORDER_BUTTON))

        assert driver.find_element(*BurgerLocators.ACTIVE_LINE)

    def test_go_to_section_sauces(self, driver):
        driver.get(Config.URL)

        driver.find_element(*BurgerLocators.LOGIN_TO_ACCOUNT_BUTTON).click()

        driver.find_element(*BurgerLocators.EMAIL_FIELD).send_keys(Config.EMAIL)
        driver.find_element(*BurgerLocators.PASSWORD_FIELD).send_keys(Config.PASSWORD)
        driver.find_element(*BurgerLocators.LOGIN_BUTTON).click()

        WebDriverWait(driver, Config.TIMEOUT).until(expected_conditions.visibility_of_element_located(BurgerLocators.ORDER_BUTTON))

        driver.find_element(*BurgerLocators.SAUCES_TEXT).click()

        WebDriverWait(driver, Config.TIMEOUT).until(expected_conditions.visibility_of_element_located(BurgerLocators.ORDER_BUTTON))

        assert driver.find_element(*BurgerLocators.ACTIVE_LINE)
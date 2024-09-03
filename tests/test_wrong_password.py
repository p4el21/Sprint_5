from src.config import Config, TestData
from src.locators import BurgerLocators

class TestWrongPassword:
    def test_wrong_password(self, driver):
        driver.get(Config.URL)
        driver.find_element(*BurgerLocators.LOGIN_TO_ACCOUNT_BUTTON).click()
        driver.find_element(*BurgerLocators.REGISTRATION_LINK).click()
        driver.find_element(*BurgerLocators.NAME_FIELD).send_keys(TestData.NAME)
        driver.find_element(*BurgerLocators.EMAIL_FIELD).send_keys(TestData.EMAIL)
        driver.find_element(*BurgerLocators.PASSWORD_FIELD).send_keys(TestData.WRONG_PASSWORD)
        driver.find_element(*BurgerLocators.REGISTRATION_BUTTON).click()
        assert driver.find_element(*BurgerLocators.ERROR_INPUT).text == 'Некорректный пароль'

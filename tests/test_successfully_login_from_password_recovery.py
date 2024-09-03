from src.config import Config
from src.locators import BurgerLocators

class TestRecovery:
    def test_successfully_login_from_password_recovery(self, driver):
        driver.get(Config.URL)
        driver.find_element(*BurgerLocators.LOGIN_TO_ACCOUNT_BUTTON).click()
        driver.find_element(*BurgerLocators.FORGOT_PASSWORD_LINK).click()
        assert driver.current_url == f'{Config.URL}/forgot-password'

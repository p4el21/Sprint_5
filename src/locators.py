from selenium.webdriver.common.by import By

class BurgerLocators:
    NAME_FIELD = By.XPATH, '//label[contains(text(), "Имя")]/following-sibling::input'
    EMAIL_FIELD = By.XPATH, '//label[contains(text(), "Email")]/following-sibling::input'
    PASSWORD_FIELD = By.XPATH, '//input[@type="password"]'
    REGISTRATION_BUTTON = By.XPATH, '//button[contains(text(), "Зарегистрироваться")]'
    REGISTRATION_LINK = By.LINK_TEXT, 'Зарегистрироваться'
    LOGOUT_BUTTON = By.XPATH, '//button[contains(text(), "Выход")]'
    LOGIN_BUTTON = By.XPATH, '//button[contains(text(), "Войти")]'
    LOGIN_TO_ACCOUNT_BUTTON = By.XPATH, '//*[contains(@class, "button_button")]'
    ORDER_BUTTON = By.XPATH, '//button[contains(text(), "Оформить заказ")]'
    BURGER_TEXT = By.XPATH, '//h1[contains(text(), "Соберите бургер")]'
    ERROR_INPUT = By.CLASS_NAME, "input__error"
    FORGOT_PASSWORD_LINK = By.XPATH, "//a[@href='/forgot-password']"
    LOGIN_LINK = By.XPATH, "//a[@href='/login']"
    PERSONAL_ACCOUNT_BUTTON = By.XPATH, "//a[@href='/account']"
    ACCOUNT_LIST = By.XPATH, '//ul[contains(@class, "Account_list")]'
    COSTRUCTOR_BUTTON = By.XPATH, "//a[contains(@class, 'AppHeader_header') and @href='/']"
    LOGO_BUTTON = By.XPATH, '//a[@href="/"]'
    BUNS_TEXT = By.XPATH, '//span[contains(text(), "Булки")]'
    FILLINGS_TEXT = By.XPATH, '//span[contains(text(), "Начинки")]'
    SAUCES_TEXT = By.XPATH, '//span[contains(text(), "Соусы")]'
    ACTIVE_LINE = By.CSS_SELECTOR, '[class*="tab_tab_type_current"]'
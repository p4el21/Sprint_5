from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get('https://stellarburgers.nomoreparties.site/')

driver.find_element(By.XPATH, '//button[contains(text(), "Войти в аккаунт")]').click()
driver.find_element(By.XPATH, '//label[contains(text(), "Email")]/following-sibling::input').send_keys('evgeniyandreev10999@mail.ru')
driver.find_element(By.XPATH, '//input[@type="password"]').send_keys('12345678')
driver.find_element(By.XPATH, '//button[contains(text(), "Войти")]').click()
driver.find_element(By.XPATH, '//a[@href="/account"]').click()

driver.find_element(By.XPATH, '//a[@href="/"]').click()

WebDriverWait(driver, 2).until(expected_conditions.visibility_of_element_located((By.XPATH, '//h1[contains(text(), "Соберите бургер")]')))
assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'
driver.quit()

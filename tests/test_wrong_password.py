from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://stellarburgers.nomoreparties.site/')

driver.find_element(By.XPATH, '//*[contains(@class, "button_button")]').click()
driver.find_element(By.LINK_TEXT, 'Зарегистрироваться').click()

driver.find_element(By.XPATH, '//label[contains(text(), "Имя")]/following-sibling::input').send_keys('Евгений')
driver.find_element(By.XPATH, '//label[contains(text(), "Email")]/following-sibling::input').send_keys('evgeniyandreev10999@mail.ru')
driver.find_element(By.XPATH, '//input[@type="password"]').send_keys('12345')
driver.find_element(By.XPATH, '//button[contains(text(), "Зарегистрироваться")]').click()

assert driver.find_element(By.CLASS_NAME, "input__error").text == 'Некорректный пароль'

driver.quit()

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://stellarburgers.nomoreparties.site/')

driver.find_element(By.XPATH, '//*[contains(@class, "button_button")]').click()
driver.find_element(By.XPATH, "//a[@href='/forgot-password']").click()

assert driver.current_url == 'https://stellarburgers.nomoreparties.site/forgot-password'
driver.quit()

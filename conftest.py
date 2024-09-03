from random import random
import random
import pytest
from selenium import webdriver
from src.config import Config

def browser_settings():
    chrome_options = webdriver.ChromeOptions()
    #chrome_options.add_argument('--headless')
    #width, height = Config.RESOLUTION
    #chrome_options.add_argument(f'--window-size={width}, {height}')
    return chrome_options

@pytest.fixture
def driver():
    chrome = webdriver.Chrome()
    chrome.maximize_window()
    chrome.get(Config.URL)
    yield chrome
    chrome.quit()

@pytest.fixture
def generate_data():
    data = 'evgeniyandreev10'
    domain = 'yandex.com'
    numbers = random.randint(100, 999)
    email = f'{data}{numbers}@{domain}'
    password = random.randint(100000, 999999)
    return email, password
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
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


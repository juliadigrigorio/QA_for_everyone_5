import pytest
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://www.saucedemo.com/')

def test_title():
    title_site = driver.title
    assert title_site == 'Swag Labs'
    time.sleep(3)

def test_login_page():
    user_name = driver.find_element(By.CSS_SELECTOR, '#user-name')
    user_name.send_keys('standard_user')
    time.sleep(3)


    password = driver.find_element(By.XPATH, '//*[@id="password"]')
    password.send_keys('secret_sauce')
    time.sleep(3)


    button_login = driver.find_element(By.CSS_SELECTOR, '#login-button')
    button_login.click()
    time.sleep(5)

    assert driver.current_url == 'https://www.saucedemo.com/inventory.html', 'WRONG!'

    driver.quit()




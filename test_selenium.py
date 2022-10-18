import time
import pytest
from webbrowser import BaseBrowser
from selenium import webdriver
# driver = webdriver.Chrome()
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('http://suninjuly.github.io/cats.html')


# time.sleep(5)
# cat = driver.find_element(By.XPATH,'/html/body/main/div/div/div/div[1]/div/div/div/div/button[1]').click()
# time.sleep(5)

def test_cat():
    cat_text = driver.find_element(By.XPATH,'//p[text()="Bullet cat"]').text
    assert cat_text == 'Bullet cat', 'WRONG!'
    time.sleep(5)

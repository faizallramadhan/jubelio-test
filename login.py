from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
import time

@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_login(driver):
    driver.get("https://app.jubelio.com/login")
    
    email_input = driver.find_element(By.NAME, "email")
    password_input = driver.find_element(By.NAME, "password")
    email_input.send_keys("qa.rakamin.jubelio@gmail.com")
    password_input.send_keys("Jubelio123!")

    login_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div[1]/div/div[2]/div/form/button')
    login_button.click()

    dashboard_title = WebDriverWait(driver, 10).until(
        EC.title_contains("Selamat Datang")
    )

    driver.save_screenshot('screenshot/login.png')
    assert "Selamat Datang" in driver.title
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def login_test(driver):
    driver.get("https://https://app.jubelio.com/login")
    
    username_input = driver.find_element(By.ID, "username")
    password_input = driver.find_element(By.ID, "password")
    username_input.send_keys("your_username")
    password_input.send_keys("your_password")

    # Submit the login form
    login_button = driver.find_element(By.ID, "login-button")
    login_button.click()

    # Wait for the dashboard page to load
    dashboard_title = WebDriverWait(driver, 10).until(
        EC.title_contains("Dashboard")
    )

    # Verify the successful login by checking the title of the dashboard page
    assert "Dashboard" in driver.title, "Login failed!"



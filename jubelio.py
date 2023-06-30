import pytest
from selenium import webdriver
from pytest_html import attach
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def login_test(driver):
    driver.get("https://https://app.jubelio.com/login")



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

def test_stock(driver):
    driver.get("https://app.jubelio.com/login")
    
    email_input = driver.find_element(By.NAME, "email")
    password_input = driver.find_element(By.NAME, "password")
    email_input.send_keys("qa.rakamin.jubelio@gmail.com")
    password_input.send_keys("Jubelio123!")

    login_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div[1]/div/div[2]/div/form/button')
    login_button.click()

    menu_barang = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="wrapper"]/nav/div/div/ul/li[2]/a/span[1]'))
    )
    menu_barang.click()
    
    persediaan = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="wrapper"]/nav/div/div/ul/li[2]/ul/li[2]/a/span'))
    )
    persediaan.click()

    penyesuaian = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div[3]/div/div[3]/div/div/div/div[2]/div/div/div/div/div/div[1]/div[2]/div/button[2]'))
    )
    penyesuaian.click()

    scan = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="page-wrapper"]/div[3]/div/div/div/div[2]/div/div/div/div/div[1]/div/div[1]/div[1]/div[2]/div/div/div/input'))
    )
    scan.send_keys("MAM2")
    
    scan_btn = driver.find_element(By.XPATH, '//*[@id="page-wrapper"]/div[3]/div/div/div/div[2]/div/div/div/div/div[1]/div/div[1]/div[1]/div[2]/div/div/div/span/button')
    scan_btn.click()

    # stockCol = WebDriverWait(driver, 10).until(
    #         EC.visibility_of_element_located((By.XPATH, '//*[@id="page-wrapper"]/div[3]/div/div/div/div[2]/div/div/div/div/div[1]/div/div[2]/div/div/div[2]/div/div[2]/div/div/div[2]/div/div/div[2]/div[1]/div/div[2]/div/div/span/div/div'))
    # )
    time.sleep(2)
    simpan_btn = driver.find_element(By.XPATH, '//*[@id="page-wrapper"]/div[3]/div/div/div/div[2]/div/div/div/div/div[3]/div/button')
    simpan_btn.click()

    time.sleep(2)
    expected_text =  "Data berhasil disimpan"
    page_source = driver.page_source
    
    driver.save_screenshot('screenshot/tambah-stock.png')
    assert expected_text in page_source

def test_stock2(driver):
    driver.get("https://app.jubelio.com/login")
    
    email_input = driver.find_element(By.NAME, "email")
    password_input = driver.find_element(By.NAME, "password")
#     email_input.send_keys("qa.rakamin.jubelio@gmail.com")
    password_input.send_keys("Jubelio123!")

    login_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div[1]/div/div[2]/div/form/button')
    login_button.click()

    menu_barang = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="wrapper"]/nav/div/div/ul/li[2]/a/span[1]'))
    )
    menu_barang.click()
    
    persediaan = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="wrapper"]/nav/div/div/ul/li[2]/ul/li[2]/a/span'))
    )
    persediaan.click()

    penyesuaian = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div[3]/div/div[3]/div/div/div/div[2]/div/div/div/div/div/div[1]/div[2]/div/button[2]'))
    )
    penyesuaian.click()

    scan = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="page-wrapper"]/div[3]/div/div/div/div[2]/div/div/div/div/div[1]/div/div[1]/div[1]/div[2]/div/div/div/input'))
    )
    scan.send_keys("MAM2")
    
    scan_btn = driver.find_element(By.XPATH, '//*[@id="page-wrapper"]/div[3]/div/div/div/div[2]/div/div/div/div/div[1]/div/div[1]/div[1]/div[2]/div/div/div/span/button')
    scan_btn.click()

    cb = driver.find_element(By.XPATH, '//*[@id="page-wrapper"]/div[3]/div/div/div/div[2]/div/div/div/div/div[1]/div/div[2]/div/div/div[3]/div/div[2]/div/div/div[2]/div/div/div[2]/div[1]/div/div[13]/div/div/span/div/label')
    cb.click()

    del_btn = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="x-delete-button"]'))
    )
    del_btn.click()

    del_btn2 = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="x-delete-button-confirm"]'))
    )
    del_btn2.click()
    
    # stockCol = WebDriverWait(driver, 10).until(
    #         EC.visibility_of_element_located((By.XPATH, '//*[@id="page-wrapper"]/div[3]/div/div/div/div[2]/div/div/div/div/div[1]/div/div[2]/div/div/div[2]/div/div[2]/div/div/div[2]/div/div/div[2]/div[1]/div/div[2]/div/div/span/div/div'))
    # )
    time.sleep(2)
    expected_text =  "Data berhasil dihapus"
    page_source = driver.page_source
    
    driver.save_screenshot('screenshot/hapus-stock.png')
    assert expected_text in page_source

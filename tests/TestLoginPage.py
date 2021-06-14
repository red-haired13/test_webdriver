import pytest
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By

@pytest.mark.parametrize("url", ['https://www.opencart.com/index.php?route=account/login'])
def test_present_email(url):
    driver = webdriver.ChromeRemoteConnection(url)
    try:
        driver.find_element(By.XPATH, '//*[@id="input-email"]')
    except NoSuchElementException:
        return False
    return True

def test_present_password(url):
    driver = webdriver.ChromeRemoteConnection(url)
    try:
        driver.find_element(By.XPATH, '//*[@id="input-password"]')
    except NoSuchElementException:
        return False
    return True

def test_present_button(url):
    driver = webdriver.ChromeRemoteConnection(url)
    try:
        driver.find_element(By.XPATH, '//*[@id="account-login"]/div[2]/div/div[1]/form/div[3]/div[1]/button[1]')
    except NoSuchElementException:
        return False
    return True

def test_present_forgot(url):
    driver = webdriver.ChromeRemoteConnection(url)
    try:
        driver.find_element(By.XPATH, '//*[@id="account-login"]/div[2]/div/div[1]/form/div[3]/div[2]/a')
    except NoSuchElementException:
        return False
    return True

def test_present_create(url):
    driver = webdriver.ChromeRemoteConnection(url)
    try:
        driver.find_element(By.XPATH, '//*[@id="account-login"]/div[2]/div/div[2]/p/a')
    except NoSuchElementException:
        return False
    return True
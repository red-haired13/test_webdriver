import pytest
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By


@pytest.mark.parametrize("url", ['https://www.opencart.com/index.php?route=marketplace/extension'])
def test_present_category(url):
    driver = webdriver.ChromeRemoteConnection(url)
    try:
        driver.find_element(By.CLASS_NAME, 'Category')
    except NoSuchElementException:
        return False
    return True


def test_present_languages(url):
    driver = webdriver.ChromeRemoteConnection(url)
    try:
        driver.find_element(By.XPATH, '//*[@id="extension-category"]/ul/li[4]/a')
    except NoSuchElementException:
        return False
    return True


def test_present_reports(url):
    driver = webdriver.ChromeRemoteConnection(url)
    try:
        driver.find_element(By.XPATH, '//*[@id="extension-category"]/ul/li[10]/a')
    except NoSuchElementException:
        return False
    return True


def test_present_menu(url):
    driver = webdriver.ChromeRemoteConnection(url)
    try:
        driver.find_element(By.XPATH, '/html/body/header/nav/div/div[1]/button/span[2]')
    except NoSuchElementException:
        return False
    return True


def test_present_logo(url):
    driver = webdriver.ChromeRemoteConnection(url)
    try:
        driver.find_element(By.XPATH, '/html/body/header/nav/div/div[1]/a/img')
    except NoSuchElementException:
        return False
    return True

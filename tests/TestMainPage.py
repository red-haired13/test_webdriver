import pytest
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By


@pytest.mark.parametrize("url", ['https://www.opencart.com/index.php?route=common/home'])
def test_present_freedownload(url):
    driver = webdriver.ChromeRemoteConnection(url)
    try:
        driver.find_element(By.XPATH, '//*[@id="hero"]/div[1]/div[1]/div/p[2]/a[1]')
    except NoSuchElementException:
        return False
    return True


def test_present_opensource(url):
    driver = webdriver.ChromeRemoteConnection(url)
    try:
        driver.find_element(By.XPATH, '//*[@id="feature"]/div[2]/div[1]/h4/div')
    except NoSuchElementException:
        return False
    return True


def test_present_extension(url):
    driver = webdriver.ChromeRemoteConnection(url)
    try:
        driver.find_element(By.XPATH, '//*[@id="feature"]/div[4]/div[1]/h4/div')
    except NoSuchElementException:
        return False
    return True


def test_present_powerful(url):
    driver = webdriver.ChromeRemoteConnection(url)
    try:
        driver.find_element(By.XPATH, '//*[@id="feature"]/div[3]/div[2]/h4/div')
    except NoSuchElementException:
        return False
    return True


def test_present_support(url):
    driver = webdriver.ChromeRemoteConnection(url)
    try:
        driver.find_element(By.XPATH, '//*[@id="feature"]/div[4]/div[2]/h4/div')
    except NoSuchElementException:
        return False
    return True

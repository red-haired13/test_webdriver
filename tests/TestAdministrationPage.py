import pytest
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By


@pytest.mark.parametrize("url", ['http://docs.opencart.com/en-gb/administration/'])
def test_present_language(url):
    driver = webdriver.ChromeRemoteConnection(url)
    try:
        driver.find_element(By.XPATH, '//*[@id="documentation"]/div[3]/div/div[2]/div[1]/button')
    except NoSuchElementException:
        return False
    driver.quit()
    return True


def test_present_filter(url):
    driver = webdriver.ChromeRemoteConnection(url)
    try:
        driver.find_element(By.XPATH, '//*[@id="en-gb"]/ul/li[7]/ul/li[2]/a')
    except NoSuchElementException:
        return False
    return True


def test_present_image_manager(url):
    driver = webdriver.ChromeRemoteConnection(url)
    try:
        driver.find_element(By.XPATH, '//*[@id="en-gb"]/ul/li[7]/ul/li[3]/a')
    except NoSuchElementException:
        return False
    return True


def test_present_doc(url):
    driver = webdriver.ChromeRemoteConnection(url)
    try:
        driver.find_element(By.XPATH, '//*[@id="documentation"]/div[3]/div/div[2]/p[4]/a')
    except NoSuchElementException:
        return False
    return True


def test_present_text(url):
    driver = webdriver.ChromeRemoteConnection(url)
    try:
        driver.find_element(By.LINK_TEXT, 'Admin Interface')
    except NoSuchElementException:
        return False
    return True

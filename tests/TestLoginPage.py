from selenium.common.exceptions import NoSuchElementException
from conftest import opencart


def test_present_content(browser):
    browser.get(opencart + 'login')
    try:
        browser.find_element_by_css_selector('#content > div > div:nth-child(1) > div > a')
    except NoSuchElementException:
        return False
    return True


def test_present_email(browser):
    browser.get(opencart + '/login')
    try:
        browser.find_element_by_css_selector('#input-email')
    except NoSuchElementException:
        return False
    return True


def test_present_password(browser):
    browser.get(opencart + '/login')
    try:
        browser.find_element_by_css_selector('#input-password')
    except NoSuchElementException:
        return False
    return True


def test_present_button(browser):
    browser.get(opencart + '/login')
    try:
        browser.find_element_by_css_selector('#content > div > div:nth-child(2) > div > form > input')
    except NoSuchElementException:
        return False
    return True


def test_present_cart_btn(browser):
    browser.get(opencart + '/login')
    try:
        browser.find_element_by_css_selector('#cart > button')
    except NoSuchElementException:
        return False
    return True

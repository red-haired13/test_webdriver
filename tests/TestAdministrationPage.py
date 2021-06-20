from selenium.common.exceptions import NoSuchElementException
from conftest import opencart


def test_present_btn(browser):
    browser.get(opencart + '/admin')
    try:
        browser.find_element_by_css_selector(
            '#content > div > div > div > div > div.panel-body > form > div.text-right > button')
    except NoSuchElementException:
        return False
    return True


def test_present_username(browser):
    browser.get(opencart + '/admin')
    try:
        browser.find_element_by_css_selector('#input-username')
    except NoSuchElementException:
        return False
    return True


def test_present_password(browser):
    browser.get(opencart + '/admin')
    try:
        browser.find_element_by_css_selector('#input-password')
    except NoSuchElementException:
        return False
    return True


def test_present_logo(browser):
    browser.get(opencart + '/admin')
    try:
        browser.find_element_by_css_selector('#header-logo > a > img')
    except NoSuchElementException:
        return False
    return True


def test_present_forgotten(browser):
    browser.get(opencart + '/admin')
    try:
        browser.find_element_by_css_selector(
            '#content > div > div > div > div > div.panel-body > form > div:nth-child(2) > span > a')
    except NoSuchElementException:
        return False
    return True

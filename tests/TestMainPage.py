from selenium.common.exceptions import NoSuchElementException
from conftest import opencart


def test_present_сartotal(browser):
    browser.get(opencart)
    try:
        browser.find_element_by_css_selector('#cart-total')
    except NoSuchElementException:
        return False
    return True


def test_present_desktops(browser):
    browser.get(opencart)
    try:
        browser.find_element_by_css_selector(
            '#menu > div.collapse.navbar-collapse.navbar-ex1-collapse > ul > li:nth-child(1) > a')
    except NoSuchElementException:
        return False
    return True


def test_present_phone(browser):
    browser.get(opencart)
    try:
        browser.find_element_by_css_selector('#top-links > ul > li:nth-child(1) > a > i')
    except NoSuchElementException:
        return False
    return True


def test_present_myaccount(browser):
    browser.get(opencart)
    try:
        browser.find_element_by_css_selector('#top-links > ul > li.dropdown > a > i')
    except NoSuchElementException:
        return False
    return True


def test_present_search(browser):
    browser.get(opencart)
    try:
        browser.find_element_by_css_selector('#search > span > button > i')
    except NoSuchElementException:
        return False
    return True

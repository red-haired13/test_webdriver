from selenium.common.exceptions import NoSuchElementException
from conftest import opencart


def test_present_components(browser):
    browser.get(opencart + '/category')
    try:
        browser.find_element_by_css_selector('#content > div > div > ul > li:nth-child(1) > a')
    except NoSuchElementException:
        return False
    return True


def test_present_menu(browser):
    browser.get(opencart + '/index.php?route=product/category&path=25')
    try:
        browser.find_element_by_css_selector('#column-left > div.list-group > a.list-group-item.active')
    except NoSuchElementException:
        return False
    return True


def test_present_home(browser):
    browser.get(opencart + '/index.php?route=product/category&path=25')
    try:
        browser.find_element_by_css_selector('#product-category > ul > li:nth-child(1) > a > i')
    except NoSuchElementException:
        return False
    return True


def test_present_aboutus(browser):
    browser.get(opencart + '/index.php?route=product/category&path=25')
    try:
        browser.find_element_by_css_selector('body > footer > div > div > div:nth-child(1) > ul > li:nth-child(1) > a')
    except NoSuchElementException:
        return False
    return True


def test_present_logo(browser):
    browser.get(opencart + '/index.php?route=product/category&path=25')
    try:
        browser.find_element_by_css_selector('#logo > h1 > a')
    except NoSuchElementException:
        return False
    return True

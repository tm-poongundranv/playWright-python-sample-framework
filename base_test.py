import pytest
from playwright.sync_api import sync_playwright
from playwright.async_api import async_playwright


class BaseTest:
    browser = None
    page = None

    @staticmethod
    def setup_base():
        with sync_playwright() as p:
            BaseTest.browser = p.chromium.launch(headless=False)
            BaseTest.page = BaseTest.browser.new_page()
            print('Page creation..')

    @staticmethod
    def teardown_base():
        BaseTest.page.close()
        BaseTest.browser.close()

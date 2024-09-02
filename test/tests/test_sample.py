import allure
import pytest
from base_test import BaseTest


class TestGoogle:
    @allure.title("")
    @allure.description("")
    @allure.severity(allure.severity_level.MINOR)
    @allure.label('owner', 'Automation')
    @allure.testcase("")
    @pytest.mark.search
    def test_google(self, page):
        page.goto('https://google.com')
        assert page.title() == 'Google'

    @allure.title("")
    @allure.description("")
    @allure.severity(allure.severity_level.MINOR)
    @allure.label('owner', 'Automation')
    @allure.testcase("")
    @pytest.mark.search
    def test_yahoo(self, page):
        page.goto('https://in.search.yahoo.com/')
        assert page.title() == 'Yaho Search - Web Search'

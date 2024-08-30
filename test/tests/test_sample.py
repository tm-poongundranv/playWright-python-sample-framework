import allure
import pytest


@allure.title("")
@allure.description("")
@allure.severity(allure.severity_level.MINOR)
@allure.label('owner', 'Automation')
@allure.testcase("")
@pytest.mark.search
def test_login(page):
    page.goto('https://google.com')
    assert page.title() == 'Google'
    png_bytes = page.screenshot(type='png')
    allure.attach(
        png_bytes,
        name="Search results",
        attachment_type=allure.attachment_type.PNG
    )

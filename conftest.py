import os
import subprocess

import allure
import pytest
import pytest_html
from playwright.sync_api import sync_playwright

from base_test import BaseTest


# @pytest.fixture
# def setup(request):
#     base = BaseTest()
#     base.setup_base()
#     yield
#     base.teardown_base()

@pytest.fixture(scope='session')
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        yield browser
        browser.close()


@pytest.fixture(scope='session')
def page(browser):
    page = browser.new_page()
    yield page
    page.close()


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    result = outcome.get_result()
    page = item.funcargs.get('page')
    if result.when == 'call' and result.failed and page:
        png_bytes = page.screenshot(type='png')
        allure.attach(
            png_bytes,
            name="Failure screenshot",
            attachment_type=allure.attachment_type.PNG
        )


@pytest.hookimpl(tryfirst=True)
def pytest_sessionfinish(session, exitstatus):
    allure_results_dir = "test/tests/artifacts/allure_report"
    allure_report_dir = "test/tests/artifacts/combine_allure_report"
    single_html_file = os.path.join(allure_report_dir, "index.html")
    if os.path.exists(single_html_file):
        try:
            os.remove(single_html_file)
            print(f"Removed existing HTML report: {single_html_file}")
        except Exception as e:
            print(f"Error removing existing HTML report: {e}")

    os.makedirs(allure_report_dir, exist_ok=True)

    command = f"allure generate {allure_results_dir} --output {allure_report_dir} --single-file"

    try:
        subprocess.run(command, shell=True, check=True)
        print(f"Allure report generated and saved to {allure_report_dir}/index.html")
    except subprocess.CalledProcessError as e:
        print(f"Error executing Allure command: {e}")

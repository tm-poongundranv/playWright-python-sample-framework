import allure
import pytest
from test.page_objects.common import Common, Actions
from test.page_objects.components import ComponentsPage
from test.page_objects.login_page import LoginPage
from playwright.sync_api import Page

from test.page_objects.shop import ShopPage


class TestPlaygroundApp:

    @allure.title("Verify user is able to filter product by brand")
    @allure.description("")
    @allure.severity(allure.severity_level.MINOR)
    @allure.label('owner', 'Automation')
    @allure.testcase("TC001")
    @pytest.mark.search
    def test_filter_product(self, page:Page):
        # Go to the Application
        page.goto('https://www.playground.testingmavens.tools/')

        # Log in using methods from LoginPage
        LoginPage.enter_user_name(page, "playground")
        LoginPage.enter_password(page, "playground@TM")
        LoginPage.click_sign_in_button(page)

        # Open the Shop Page
        Common.open_shop_page(page)
        ShopPage.click_shop_by_brand(page)
        ShopPage.filter_by_brand(page, "Samsung")



    @allure.title("Verify pop up is displayed on clicking corresponding tile in Components page")
    @allure.description("")
    @allure.severity(allure.severity_level.MINOR)
    @allure.label('owner', 'Automation')
    @allure.testcase("TC002")
    @pytest.mark.search
    def test_component_page(self,page: Page):
        # Go to the main page
        page.goto('https://www.playground.testingmavens.tools/')

        # Log in using static methods from LoginPage
        LoginPage.enter_user_name(page, "playground")
        LoginPage.enter_password(page, "playground@TM")
        LoginPage.click_sign_in_button(page)

        # Open the Components Page using Common's static method
        Common.open_components_page(page)

        # Ensure that the Components page is loaded
        page.locator('text=Pop Window Component').wait_for()

        # Use static methods from ComponentsPage
        ComponentsPage.open_pop_window_and_verify(page)


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
        # Initialize the LoginPage, Common , ShopPage
        common_obj = Common(page)
        login_page_obj = LoginPage(page)
        shop_obj = ShopPage(page)
        # Go to the Application
        page.goto('https://www.playground.testingmavens.tools/')

        # Log in using methods from LoginPage
        login_page_obj.enter_user_name("playground")
        login_page_obj.enter_password("playground@TM")
        login_page_obj.click_sign_in_button()

        # Open the Shop Page
        common_obj.open_shop_page()
        shop_obj.click_shop_by_brand()
        shop_obj.filter_by_brand("Samsung")



    @allure.title("Verify pop up is displayed on clicking corresponding tile in Components page")
    @allure.description("")
    @allure.severity(allure.severity_level.MINOR)
    @allure.label('owner', 'Automation')
    @allure.testcase("TC002")
    @pytest.mark.search
    def test_component_page(self,page: Page):
        # Initialize the LoginPage
        login_page_obj = LoginPage(page)

        # Go to the main page
        page.goto('https://www.playground.testingmavens.tools/')

        # Log in using methods from LoginPage
        login_page_obj.enter_user_name("playground")
        login_page_obj.enter_password("playground@TM")
        login_page_obj.click_sign_in_button()

        # Open the Components Page
        common_obj = Common(page)
        common_obj.open_components_page()

        # Ensure that the Components page is loaded
        page.locator('text=Pop Window Component').wait_for()
        components_obj = ComponentsPage(page)

        # Click on the tile that opens the pop-up (assuming the selector for the tile)
        components_obj.open_pop_window_and_verify()



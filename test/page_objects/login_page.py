import allure
from playwright.sync_api import Page, Locator, expect
from test.page_objects.common import Common, Actions


class LoginPage:

    @staticmethod
    @allure.step("Enter username")
    def enter_user_name(page: Page, user_name: str):
        """
        Enters the username into the username field and captures a screenshot.

        Args:
            page (Page): The page instance where the action is performed.
            user_name (str): The username to be entered.
        """
        email_field = page.locator('input[placeholder="Username"]')
        Actions.type_text(email_field, user_name, "User name field")
        Common.capture_screenshot(page, "Entered Username")

    @staticmethod
    @allure.step("Enter password")
    def enter_password(page: Page, password: str):
        """
        Enters the password into the password field and captures a screenshot.

        Args:
            page (Page): The page instance where the action is performed.
            password (str): The password to be entered.
        """
        password_field = page.locator('input[placeholder="Password"]')
        Actions.type_text(password_field, password, "Password field")
        Common.capture_screenshot(page, "Entered Password")

    @staticmethod
    @allure.step("Click sign-in button")
    def click_sign_in_button(page: Page):
        """
        Clicks the sign-in button and captures a screenshot.

        Args:
            page (Page): The page instance where the action is performed.
        """
        sign_in_button = page.locator('text=Sign In')
        Actions.click_button(sign_in_button, "Sign In button")
        Common.capture_screenshot(page, "Clicked Sign-In Button")

    @staticmethod
    @allure.step("Click login option")
    def click_login_option(page: Page):
        """
        Clicks the login option and captures a screenshot.

        Args:
            page (Page): The page instance where the action is performed.
        """
        login_option = page.locator('text=Login')
        Actions.click_button(login_option, "Login option")
        Common.capture_screenshot(page, "Clicked Login Option")

    @staticmethod
    @allure.step("Enter email address")
    def enter_email_address(page: Page, email_address: str):
        """
        Enters the email address into the email address field.

        Args:
            page (Page): The page instance where the action is performed.
            email_address (str): The email address to be entered.
        """
        email_address_field = page.locator("//input[@name='email']")
        Actions.type_text(email_address_field, email_address, "Email address field")

    @staticmethod
    @allure.step("Enter ecommerce password")
    def enter_ecommerce_password(page: Page, password: str):
        """
        Enters the password into the ecommerce password field.

        Args:
            page (Page): The page instance where the action is performed.
            password (str): The password to be entered.
        """
        ecommerce_password_field = page.locator("//input[@name='password']")
        Actions.type_text(ecommerce_password_field, password, "Password field")

    @staticmethod
    @allure.step("Click login button")
    def click_login_button(page: Page):
        """
        Clicks the login button and captures a screenshot.

        Args:
            page (Page): The page instance where the action is performed.
        """
        login_button = page.locator("//button[text()='Login']")
        Actions.click_button(login_button, "Login button")
        Common.capture_screenshot(page, "Clicked Login Button")

    @staticmethod
    def profile_dropdown(page: Page) -> Locator:
        """
        Returns the locator for the profile dropdown icon.

        Args:
            page (Page): The page instance where the locator is used.

        Returns:
            Locator: The locator for the profile dropdown.
        """
        return page.locator("//*[name()='svg'][@class='text-black']")

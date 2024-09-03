from playwright.sync_api import Page, Locator, expect
from test.page_objects.common import Actions


class LoginPage:
    @staticmethod
    def enter_user_name(page: Page, user_name: str):
        email_field = page.locator('input[placeholder="Username"]')
        Actions.type_text(email_field, user_name, "User name field")

    @staticmethod
    def enter_password(page: Page, password: str):
        password_field = page.locator('input[placeholder="Password"]')
        Actions.type_text(password_field, password, "Password field")

    @staticmethod
    def click_sign_in_button(page: Page):
        sign_in_button = page.locator('text=Sign In')
        Actions.click_button(sign_in_button, "Sign In button")

    @staticmethod
    def click_login_option(page: Page):
        login_option = page.locator('text=Login')
        Actions.click_button(login_option, "Login option")

    @staticmethod
    def enter_email_address(page: Page, email_address: str):
        email_address_field = page.locator("//input[@name='email']")
        Actions.type_text(email_address_field, email_address, "Email address field")

    @staticmethod
    def enter_ecommerce_password(page: Page, password: str):
        ecommerce_password_field = page.locator("//input[@name='password']")
        Actions.type_text(ecommerce_password_field, password, "Password field")

    @staticmethod
    def click_login_button(page: Page):
        login_button = page.locator("//button[text()='Login']")
        Actions.click_button(login_button, "Login button")

    @staticmethod
    def profile_dropdown(page: Page) -> Locator:
        return page.locator("//*[name()='svg'][@class='text-black']")

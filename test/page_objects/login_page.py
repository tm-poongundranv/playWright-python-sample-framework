import json
from playwright.sync_api import Page, Locator, expect
from test.page_objects.common import Common, Actions

# with open('path/to/env-test.json') as f:
#     env = json.load(f)
class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.actions = Actions(self.page)

        self.email_field = self.page.locator('input[placeholder="Username"]')
        self.password_field = self.page.locator('input[placeholder="Password"]')
        self.sign_in_button = self.page.locator('text=Sign In')

        self.login_option = self.page.locator('text=Login')
        self.email_address_field = self.page.locator("//input[@name='email']")
        self.ecommerce_password_field = self.page.locator("//input[@name='password']")
        self.login_button = self.page.locator("//button[text()='Login']")
        self.profile_dropdown = self.page.locator("//*[name()='svg'][@class='text-black']")

    def enter_user_name(self, user_name: str):
        self.actions.wait_for_page_to_load()
        self.actions.type_text(self.email_field, user_name, "User name field")

    def enter_password(self, password: str):
        self.actions.type_text(self.password_field, password, "Password field")

    def click_sign_in_button(self):
        self.actions.click_button(self.sign_in_button, "Sign In button")

    def click_login_option(self):
        self.actions.click_button(self.login_option, "Login option")

    def enter_email_address(self, email_address: str):
        self.actions.wait_for_page_to_load()
        self.actions.type_text(self.email_address_field, email_address, "Email address field")

    def enter_ecommerce_password(self, password: str):
        self.actions.type_text(self.ecommerce_password_field, password, "Password field")

    def click_login_button(self):
        self.actions.click_button(self.login_button, "Login button")

import os
from playwright.sync_api import Page, Locator, expect

class Actions:
    def __init__(self, page: Page):
        self.page = page

    def click_on(self, locator: Locator, name: str):
        locator.click()
        print(f"Clicked on {name}")

    def wait_for_page_to_load(self):
        self.page.wait_for_load_state('networkidle')
        print("Page load complete")

    @staticmethod
    def type_text(locator: Locator, text: str, name: str):
        locator.fill(text)
        print(f"Typed '{text}' into {name}")

    @staticmethod
    def click_button(locator: Locator, button_name: str):
        locator.click()
        print(f"Button '{button_name}' clicked")




class Common:
    def __init__(self, page: Page):
        self.page = page
        # Define any common locators or methods here
        self.actions = Actions(self.page)
        self.shop_menu = self.page.locator('role=link[name="Shop"]')
        self.components_menu = self.page.locator('role=link[name="Components"]')
        self.home_menu = self.page.locator('role=link[name="Home"]')
        self.products_title = self.page.locator('role=heading[name="Products"]')
        self.shop_by_brand = self.page.locator("//span[text()='Shop by Brand']")

    def launch_web_app(self):
        url =('base_url', 'http://localhost')
        self.page.goto(url)
        print(f"Navigated to the URL: {url}")

    def open_shop_page(self):
        self.actions.click_on(self.shop_menu, "Shop menu")
        self.actions.wait_for_page_to_load()
        expect(self.products_title).to_be_visible()
        print("Shop page with Products title should be visible")

    def open_components_page(self):
        self.actions.click_on(self.components_menu, "Components menu")




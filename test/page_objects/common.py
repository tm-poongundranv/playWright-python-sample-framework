import os
from playwright.sync_api import Page, Locator, expect


class Actions:
    @staticmethod
    def click_on(locator: Locator, name: str):
        locator.click()
        print(f"Clicked on {name}")

    @staticmethod
    def wait_for_page_to_load(page: Page):
        page.wait_for_load_state('networkidle')
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
    base_url = 'http://localhost'

    @staticmethod
    def launch_web_app(page: Page):
        page.goto(Common.base_url)
        print(f"Navigated to the URL: {Common.base_url}")

    @staticmethod
    def open_shop_page(page: Page):
        shop_menu = page.locator('role=link[name="Shop"]')
        products_title = page.locator('role=heading[name="Products"]')

        Actions.click_on(shop_menu, "Shop menu")
        Actions.wait_for_page_to_load(page)
        expect(products_title).to_be_visible()
        print("Shop page with Products title should be visible")

    @staticmethod
    def open_components_page(page: Page):
        components_menu = page.locator('role=link[name="Components"]')

        Actions.click_on(components_menu, "Components menu")

    @staticmethod
    def shop_by_brand_locator(page: Page) -> Locator:
        return page.locator("//span[text()='Shop by Brand']")

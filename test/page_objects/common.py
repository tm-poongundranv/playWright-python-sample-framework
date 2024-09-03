import os
import allure
from playwright.sync_api import Page, Locator, expect



class Actions:
    @staticmethod
    def click_on(locator: Locator, name: str):
        """
        Clicks on a specified element and logs the action.

        Args:
            locator (Locator): The element to be clicked.
            name (str): A descriptive name of the element for logging purposes.
        """
        locator.click()
        print(f"Clicked on {name}")

    @staticmethod
    @allure.step("Wait for page to load")
    def wait_for_page_to_load(page: Page):
        """
        Waits for the page to finish loading, ensuring that all network activity has ceased.

        Args:
            page (Page): The page instance to wait for.
        """
        page.wait_for_load_state('networkidle')
        print("Page load complete")

    @staticmethod
    def type_text(locator: Locator, text: str, name: str):
        """
        Types the specified text into an element and logs the action.

        Args:
            locator (Locator): The input field where the text will be typed.
            text (str): The text to be entered.
            name (str): A descriptive name of the field for logging purposes.
        """
        locator.fill(text)
        print(f"Typed '{text}' into {name}")

    @staticmethod
    def click_button(locator: Locator, button_name: str):
        """
        Clicks on a button and logs the action.
        Args:
            locator (Locator): The button element to be clicked.
            button_name (str): A descriptive name of the button for logging purposes.
        """
        locator.click()
        print(f"Button '{button_name}' clicked")


class Common:
    base_url = 'https://www.playground.testingmavens.tools/'

    @staticmethod
    def capture_screenshot(page: Page, step_name: str):
        """
        Captures a screenshot of the current page and attaches it to the allure report.

        Args:
            page (Page): The page instance from which to capture the screenshot.
            step_name (str): A descriptive name for the screenshot, used in the allure report.

        Attaches:
            A screenshot to the allure report with the specified step name.
        """
        screenshot = page.screenshot(type='png')
        allure.attach(
            screenshot,
            name=step_name,
            attachment_type=allure.attachment_type.PNG
        )

    @staticmethod
    @allure.step("Launch the application")
    def launch_web_app(page: Page):
        """
        Launches the web application by navigating to the base URL and captures a screenshot.

        Args:
            page (Page): The page instance to navigate.

        Logs:
            Prints a message with the URL navigated to and captures a screenshot of the launched application.
        """
        page.goto(Common.base_url)
        print(f"Navigated to the URL: {Common.base_url}")
        Common.capture_screenshot(page, "Launched the application")

    @staticmethod
    @allure.step("Navigate to shop page")
    def open_shop_page(page: Page):
        """
        Navigates to the Shop page, waits for it to load, verifies the visibility of the Products title,
        and captures a screenshot of the Shop page.

        Args:
            page (Page): The page instance to perform actions on.

        Logs:
            Prints a message indicating that the Shop page with the Products title should be visible.
        """
        shop_menu = page.locator('role=link[name="Shop"]')
        products_title = page.locator('role=heading[name="Products"]')
        Actions.click_on(shop_menu, "Shop menu")
        Actions.wait_for_page_to_load(page)
        Common.capture_screenshot(page, "Navigated to Shop page")
        expect(products_title).to_be_visible()
        print("Shop page with Products title should be visible")

    @staticmethod
    @allure.step("Navigate to Components page")
    def open_components_page(page: Page):
        """
        Navigates to the Components page, waits for it to load, and captures a screenshot.

        Args:
            page (Page): The page instance to perform actions on.

        Logs:
            Captures a screenshot of the Components page.
        """
        components_menu = page.locator('role=link[name="Components"]')
        Actions.click_on(components_menu, "Components menu")
        Actions.wait_for_page_to_load(page)
        Common.capture_screenshot(page, "Navigated to Components page")

    @staticmethod
    def shop_by_brand_locator(page: Page) -> Locator:
        """
        Provides a locator for the 'Shop by Brand' element on the page.

        Args:
            page (Page): The page instance where the locator is to be found.

        Returns:
            Locator: The locator for the 'Shop by Brand' element.
        """
        return page.locator("//span[text()='Shop by Brand']")


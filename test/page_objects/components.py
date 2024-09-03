import allure
from playwright.sync_api import Page, Locator, expect
from test.page_objects.common import Common, Actions

class ComponentsPage(Common):

    @staticmethod
    def str_brand_check_box(brand_name: str) -> str:
        """
        Constructs an XPath selector string for the checkbox of a specific brand.

        Args:
            brand_name (str): The name of the brand for which the checkbox locator is needed.

        Returns:
            str: XPath selector for the brand's checkbox.
        """
        return f"//li[text()='{brand_name}']/input"

    @staticmethod
    def filter_by_brand(page: Page, brand_name: str):
        """
        Filters products by the specified brand and verifies that the "Products" heading is visible.

        Args:
            page (Page): The page instance where the actions are performed.
            brand_name (str): The name of the brand to filter by.
        """
        brand_checkbox = page.locator(ComponentsPage.str_brand_check_box(brand_name))
        Actions.click_on(brand_checkbox, f"{brand_name} checkbox")
        Actions.wait_for_page_to_load(page)
        expect(page.locator('role=heading[name="Products"]')).to_be_visible()
        print(f"Filtered by brand {brand_name}")

    @staticmethod
    @allure.step("Open and verify pop up window component")
    def open_pop_window_and_verify(page: Page):
        """
        Opens a pop-up window, verifies its content, and then closes it. Captures screenshots at each step.

        Args:
            page (Page): The page instance where the actions are performed.
        """
        pop_window_learn_more = page.locator('.transform', has_text='Pop Window Component').locator('a')
        open_pop_window_button = page.locator('role=button[name="Open Pop Window"]')
        pop_window_content_title = page.locator('role=heading[name="Pop Window Content"]')
        close_pop_window_button = page.locator('role=button[name="Close"]')

        Actions.click_on(pop_window_learn_more, "Learn More in Pop Window tile")
        Common.capture_screenshot(page, "Opened pop up window")

        Actions.click_button(open_pop_window_button, "Open Pop Window")
        Common.capture_screenshot(page, "Clicked on pop up window")

        expect(pop_window_content_title).to_be_visible()
        Actions.click_button(close_pop_window_button, "Close Pop Window")
        Common.capture_screenshot(page, "Closed pop up window")

        expect(open_pop_window_button).to_be_enabled()
        print("Verified Pop Window and its content")



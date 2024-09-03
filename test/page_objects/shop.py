import allure
from playwright.sync_api import Page, expect, Locator
from test.page_objects.common import Actions, Common


class ShopPage:

    @staticmethod
    @allure.step("Click on 'Shop by Brand'")
    def click_shop_by_brand(page: Page):
        """
        Clicks on the 'Shop by Brand' element and captures a screenshot.

        Args:
            page (Page): The page instance where the action is performed.
        """
        shop_by_brand = page.locator("//span[text()='Shop by Brand']")
        shop_by_brand.click()  # Clicks the 'Shop by Brand' element
        Common.capture_screenshot(page, "Navigated to Shop Page")

    @staticmethod
    def brand_check_box(brand_name: str) -> str:
        """
        Returns the XPath for the checkbox associated with the given brand name.

        Args:
            brand_name (str): The name of the brand whose checkbox is to be located.

        Returns:
            str: The XPath locator string for the brand's checkbox.
        """
        return f"//li[./label[text()='{brand_name}']]//input[@type='checkbox']"

    @staticmethod
    @allure.step("Filter products by brand")
    def filter_by_brand(page: Page, brand_name: str) -> None:
        """
        Filters the products by the specified brand and verifies that the 'Products' heading is visible.

        Args:
            page (Page): The page instance where the action is performed.
            brand_name (str): The name of the brand to filter by.
        """
        brand_checkbox_locator = page.locator(ShopPage.brand_check_box(brand_name))
        Actions.click_on(brand_checkbox_locator, f"{brand_name} checkbox")
        Actions.wait_for_page_to_load(page)
        products_title = page.locator("role=heading[name='Products']")
        expect(products_title).to_be_visible()
        Common.capture_screenshot(page, "Filtered products by brand")
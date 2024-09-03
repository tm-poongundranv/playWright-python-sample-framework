from playwright.sync_api import Page, expect, Locator
from test.page_objects.common import Actions

class ShopPage:
    @staticmethod
    def click_shop_by_brand(page: Page):
        shop_by_brand = page.locator("//span[text()='Shop by Brand']")
        shop_by_brand.click()  # Correct method to click on the element
        print("Clicked on 'Shop by Brand'")

    @staticmethod
    def brand_check_box(brand_name: str) -> str:
        return f"//li[./label[text()='{brand_name}']]//input[@type='checkbox']"

    @staticmethod
    def filter_by_brand(page: Page, brand_name: str) -> None:
        brand_checkbox_locator = page.locator(ShopPage.brand_check_box(brand_name))
        Actions.click_on(brand_checkbox_locator, f"{brand_name} checkbox")
        Actions.wait_for_page_to_load(page)
        products_title = page.locator("role=heading[name='Products']")
        expect(products_title).to_be_visible()

    @staticmethod
    def get_total_products(page: Page) -> Locator:
        return page.locator("//p[contains(text(),'Products from ')]")

    @staticmethod
    def get_first_item_shown(page: Page) -> Locator:
        return page.locator("//img[contains(@alt,'/assets')]")

    @staticmethod
    def get_first_item_flex_menu(page: Page) -> Locator:
        return page.locator('.w-full > ul').first

    @staticmethod
    def get_view_details_buttons(page: Page) -> Locator:
        return page.locator("//li[text()='View Details']")

    @staticmethod
    def get_product_picture(page: Page) -> Locator:
        return page.locator("//img[@class='w-full h-full object-contain']")

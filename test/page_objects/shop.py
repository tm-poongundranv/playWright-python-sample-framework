from playwright.sync_api import Page, expect
from test.page_objects.common import Common, Actions


class ShopPage(Common, Actions):
    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page
        self.actions = Actions(self.page)
        self.products_title = self.page.locator("role=heading[name='Products']")
        self.total_products = self.page.locator("//p[contains(text(),'Products from ')]")
        self.first_item_shown = self.page.locator("//img[contains(@alt,'/assets')]")
        self.first_item_flex_menu = self.page.locator('.w-full > ul').first
        self.view_details_buttons = self.page.locator("//li[text()='View Details']")
        self.product_picture = self.page.locator("//img[@class='w-full h-full object-contain']")

    def click_shop_by_brand(self):
        # Use the Locator to perform actions
        self.shop_by_brand.click()  # Correct method to click on the element
        print("Clicked on 'Shop by Brand'")

    @staticmethod
    def brand_check_box(brand_name: str) -> str:
        return f"//li[./label[text()='{brand_name}']]//input[@type='checkbox']"

    def filter_by_brand(self, brand_name: str) -> None:
        self.actions.click_on(self.page.locator(self.brand_check_box(brand_name)), f"{brand_name} checkbox")
        self.actions.wait_for_page_to_load()
        expect(self.products_title).to_be_visible()





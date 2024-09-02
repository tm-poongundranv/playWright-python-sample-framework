from playwright.sync_api import Page, Locator, expect
from test.page_objects.common import Common

class ComponentsPage(Common):
    def __init__(self, page: Page):
        super().__init__(page)

        self.str_brand_check_box = lambda brand_name: f"//li[text()='{brand_name}']/input"
        self.home_menu = self.page.locator('role=link[name="Home"]')
        self.pop_window_learn_more = self.page.locator(
            '.transform', has_text='Pop Window Component'
        ).locator('a')
        self.open_pop_window_button = self.page.locator('role=button[name="Open Pop Window"]')
        self.pop_window_content_title = self.page.locator('role=heading[name="Pop Window Content"]')
        self.close_pop_window_button = self.page.locator('role=button[name="Close"]')
        self.shadow_dom_learn_more = self.page.locator('.transform >> text=Shadow DOM Component >> a')
        self.open_shadow_dom_title = self.page.locator('div.shadow-host:first-of-type .shadow-content .shadow-title')
        self.closed_shadow_dom_title = self.page.locator('div.shadow-host:last-of-type')
        self.name_input_box = self.page.locator("#inputForName")

    def filter_by_brand(self, brand_name: str):
        brand_checkbox = self.page.locator(self.str_brand_check_box(brand_name))
        self.actions.click_on(brand_checkbox, f"{brand_name} checkbox")
        self.actions.wait_for_page_to_load()
        expect(self.products_title).to_be_visible()
        print(f"Filtered by brand {brand_name}")

    def open_pop_window_and_verify(self):
        self.actions.click_on(self.pop_window_learn_more, "Learn More in Pop Window tile")
        self.actions.click_button(self.open_pop_window_button, "Open Pop Window")
        expect(self.pop_window_content_title).to_be_visible()
        self.actions.click_button(self.close_pop_window_button, "Close Pop Window")
        expect(self.open_pop_window_button).to_be_enabled()
        print("Verified Pop Window and its content")

    def verify_shadow_dom_open(self):
        self.actions.click_on(self.shadow_dom_learn_more, "Learn More in Shadow DOM tile")
        expect(self.open_shadow_dom_title).to_be_visible()
        open_texts = self.open_shadow_dom_title.text_content()
        print('Open texts:', open_texts)

    def verify_shadow_dom_closed(self):
        self.actions.click_on(self.shadow_dom_learn_more, "Learn More in Shadow DOM tile")
        expect(self.open_shadow_dom_title).to_be_visible()
        self.actions.click_on(self.name_input_box, "Enter name input")

        # Fill input and copy text
        self.name_input_box.click()
        self.name_input_box.fill("Arun")
        self.page.keyboard.press('Tab')
        self.page.keyboard.type('Superman')
        self.page.keyboard.press('Meta+A')
        self.page.keyboard.press('Meta+C')

        copied_text = self.page.evaluate("navigator.clipboard.readText()")
        print("Copied Text:", copied_text)

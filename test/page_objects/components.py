from playwright.sync_api import Page, Locator, expect
from test.page_objects.common import Common, Actions

class ComponentsPage(Common):
    @staticmethod
    def str_brand_check_box(brand_name: str) -> str:
        return f"//li[text()='{brand_name}']/input"

    @staticmethod
    def filter_by_brand(page: Page, brand_name: str):
        brand_checkbox = page.locator(ComponentsPage.str_brand_check_box(brand_name))
        Actions.click_on(brand_checkbox, f"{brand_name} checkbox")
        Actions.wait_for_page_to_load(page)
        expect(page.locator('role=heading[name="Products"]')).to_be_visible()
        print(f"Filtered by brand {brand_name}")

    @staticmethod
    def open_pop_window_and_verify(page: Page):
        pop_window_learn_more = page.locator(
            '.transform', has_text='Pop Window Component'
        ).locator('a')
        open_pop_window_button = page.locator('role=button[name="Open Pop Window"]')
        pop_window_content_title = page.locator('role=heading[name="Pop Window Content"]')
        close_pop_window_button = page.locator('role=button[name="Close"]')

        Actions.click_on(pop_window_learn_more, "Learn More in Pop Window tile")
        Actions.click_button(open_pop_window_button, "Open Pop Window")
        expect(pop_window_content_title).to_be_visible()
        Actions.click_button(close_pop_window_button, "Close Pop Window")
        expect(open_pop_window_button).to_be_enabled()
        print("Verified Pop Window and its content")

    @staticmethod
    def verify_shadow_dom_open(page: Page):
        shadow_dom_learn_more = page.locator('.transform >> text=Shadow DOM Component >> a')
        open_shadow_dom_title = page.locator('div.shadow-host:first-of-type .shadow-content .shadow-title')

        Actions.click_on(shadow_dom_learn_more, "Learn More in Shadow DOM tile")
        expect(open_shadow_dom_title).to_be_visible()
        open_texts = open_shadow_dom_title.text_content()
        print('Open texts:', open_texts)

    @staticmethod
    def verify_shadow_dom_closed(page: Page):
        shadow_dom_learn_more = page.locator('.transform >> text=Shadow DOM Component >> a')
        open_shadow_dom_title = page.locator('div.shadow-host:first-of-type .shadow-content .shadow-title')
        name_input_box = page.locator("#inputForName")

        Actions.click_on(shadow_dom_learn_more, "Learn More in Shadow DOM tile")
        expect(open_shadow_dom_title).to_be_visible()
        Actions.click_on(name_input_box, "Enter name input")

        # Fill input and copy text
        name_input_box.click()
        name_input_box.fill("Arun")
        page.keyboard.press('Tab')
        page.keyboard.type('Superman')
        page.keyboard.press('Meta+A')
        page.keyboard.press('Meta+C')

        copied_text = page.evaluate("navigator.clipboard.readText()")
        print("Copied Text:", copied_text)

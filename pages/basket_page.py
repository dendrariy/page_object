from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def get_basket_content_text(self):
        return self.browser.find_element(*BasketPageLocators.BASKET_CONTENT).text

    def check_empty_basket(self):
        assert "Your basket is empty" in self.get_basket_content_text(), "Text is not present on the page"
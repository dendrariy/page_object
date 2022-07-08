from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        self.browser.find_element(*ProductPageLocators.ADD_BUTTON).click()

    def get_product_name(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def get_product_price(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

    def get_added_product_name(self):
        return self.browser.find_element(*ProductPageLocators.ADDED_PRODUCT_NAME).text

    def get_added_product_price(self):
        return self.browser.find_element(*ProductPageLocators.ADDED_PRODUCT_PRICE).text

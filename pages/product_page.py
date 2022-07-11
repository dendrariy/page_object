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

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_be_dissapeared(self):
        assert  self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is not disappeared"

    def check_product_name(self, name):
        added_name = self.get_added_product_name()

        assert added_name == name, "Added name is not equal to origin"

    def check_product_price(self, price):
        basket_price = self.get_added_product_price()

        assert basket_price == price, "Basket price is not equal to origin"
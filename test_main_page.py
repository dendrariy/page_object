from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage
import pytest


@pytest.mark.skip
def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()


@pytest.mark.skip
def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_page()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/"
    page = MainPage(browser, link)
    page.open()
    page.open_basket()
    basket_page = BasketPage(browser, link)
    assert "Your basket is empty" in basket_page.get_basket_content_text(), "Text is not present on the page"
import pytest

from .pages.product_page import ProductPage
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
import time

links = ["https://selenium1py.pythonanywhere.com/ru/catalogue/"]

# def test_guest_can_go_to_login_page(browser):
#     link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
#     page = MainPage(browser, link)
#     page.open()
#     time.sleep(5)
#     page.go_to_login_page()
#     login_page = LoginPage(browser, browser.current_url)
#     login_page.should_be_login_page()
#     time.sleep(5)



# @pytest.mark.skip
# @pytest.mark.parametrize("link", links)
# def test_guest_can_add_product_to_basket(browser, link):
#     page = ProductPage(browser, link)
#     page.open()
#     page.guest_can_add_product_to_basket()
#     page.go_to_basket()
#
#     page_basket = BasketPage(browser, browser.current_url)
#     page_basket.should_check_basket(link)

# @pytest.mark.parametrize("link", links)
# def test_guest_cant_see_success_message_after_adding_product_to_basket(browser, link):
#     page = ProductPage(browser, link)
#     page.open()
#     page.guest_cant_see_success_message_after_adding_product_to_basket()
#
# @pytest.mark.parametrize("link", links)
# def test_guest_cant_see_success_message(browser, link):
#     page = ProductPage(browser, link)
#     page.open()
#     page.guest_cant_see_success_message()

# @pytest.mark.parametrize("link", links)
# def test_message_disappeared_after_adding_product_to_basket(browser, link):
#     page = ProductPage(browser, link)
#     page.open()
#     page.message_disappeared_after_adding_product_to_basket()
#
# def test_guest_should_see_login_link_on_product_page(browser):
#     link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
#     page = ProductPage(browser, link)
#     page.open()
#     page.should_be_login_link()
#
# def test_guest_can_go_to_login_page_from_product_page(browser):
#     link = "https://selenium1py.pythonanywhere.com/en-gb/catalogue/"
#     page = ProductPage(browser, link)
#     page.open()
#     page.should_be_login_link()



# @pytest.mark.skip
@pytest.mark.parametrize("link", links)
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser, link):
    page = MainPage(browser, link)
    page.open()
    page.go_to_basket_page()
    page_basket = BasketPage(browser, browser.current_url)
    page_basket.should_be_empty_basket()


# @pytest.mark.skip
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    page_basket = BasketPage(browser, browser.current_url)
    page_basket.should_be_empty_basket()
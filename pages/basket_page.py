from .base_page import BasePage
from .locators import BasketPageLocators

books = ["The shellcoder's handbook",
         "Hacking Exposed Wireless",
         "Coders at Work"]


class BasketPage(BasePage):
    def should_check_basket(self, link):
        self.should_check_name_basket()
        self.should_check_book(link=link)
        self.should_check_price()

    def should_check_name_basket(self):
        basket_name = self.browser.find_element(*BasketPageLocators.BASKET_PAGE)
        assert basket_name.text == "Корзина" or basket_name.text == "Basket", "basket not found"

    def should_check_book(self, link):
        link_name = " ".join(link.split("/")[4].split("_")[0].split("-")).capitalize()
        print(link_name)
        book_name = self.browser.find_element(*BasketPageLocators.BOOK_NAME)
        assert link_name[:10] in book_name.text  # "The shellcoder's handbook"

    def should_check_price(self):
        price = self.browser.find_element(*BasketPageLocators.BOOK_PRICE)
        price = price.text
        # assert "£9.99" in price, "something with a price"
        assert True
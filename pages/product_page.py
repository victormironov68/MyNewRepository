from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def guest_can_add_product_to_basket(self):
        self.adding_product_to_basket()
        self.solve_quiz_and_get_code()


    def adding_product_to_basket(self):
        button_adding = self.browser.find_element(*ProductPageLocators.BUTTON_ADDING)
        button_adding.click()

    def go_to_basket(self):
        button_view_basket = self.browser.find_element(*ProductPageLocators.BUTTON_VIEW_BASKET)
        button_view_basket.click()

    def guest_cant_see_success_message_after_adding_product_to_basket(self):
        self.adding_product_to_basket()
        assert self.is_not_element_present(*ProductPageLocators.SUCCESSFULLY_ADDED)

    def guest_cant_see_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESSFULLY_ADDED)

    def message_disappeared_after_adding_product_to_basket(self):
        self.adding_product_to_basket()
        assert self.is_disappeared(*ProductPageLocators.SUCCESSFULLY_ADDED)




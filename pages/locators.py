from selenium.webdriver.common.by import By



class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BUTTON_VIEW_BASKET = (By.XPATH, "//*[@id='default']/header/div[1]/div/div[2]/span/a")
    #

class MainPageLocators():
    pass

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    LOGIN_MAIL = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_PASSWORD = (By.CSS_SELECTOR, "#id_login-password")
    LOGIN_BATTON = (By.CLASS_NAME, "btn.btn-lg.btn-primary")
    REGISTRATION_MAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTRATION_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTRATION_PASSWORD_REPEAT = (By.CSS_SELECTOR, "#registration-password2")

class ProductPageLocators():
    BUTTON_ADDING = (By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket")
    SUCCESSFULLY_ADDED = (By.XPATH, "//*[@id='messages']/div[1]/div")

class BasketPageLocators():
    BASKET_PAGE = (By.XPATH, "//*[@id='default']/div[2]/div/div[1]/h1")
    BOOK_NAME = (By.XPATH, "//*[@id='basket_formset']/div/div/div[2]/h3/a")
    BOOK_PRICE = (By.XPATH, "//*[@id='basket_formset']/div/div/div[4]/p")
    BASKET_EMPTY_TEXT = (By.XPATH, "//*[@id='content_inner']/p")
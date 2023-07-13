# import time
# import math
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.common.exceptions import NoAlertPresentException
#
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# BUTTON_ADDING = (By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket")
# BOOK_PRICE = (By.CSS_SELECTOR, "..price-color.align-right")
# BASKET_PAGE = (By.XPATH, "//*[@id='default']/div[2]/div/div[1]/h1")
# #  #default > div.container-fluid.page > div > div > div > section > div > ol > li:nth-child(3) > article > div.product_price > form > button
# #//*[@id="default"]/div[2]/div/div/div/section/div/ol/li[3]/article/div[2]/form/button
#
# try:
#     browser = webdriver.Chrome()
#
#     link = "http://selenium1py.pythonanywhere.com/ru/basket/"
#     browser.get(link)
#     time.sleep(5)
#
#
#     price = browser.find_element(*BASKET_PAGE)
#     print(price.text)
#
# finally:
#     browser.quit()
#
#
#

link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
link = " ".join(link.split("/")[4].split("_")[0].split("-")).capitalize()
# link = link.capitalize()

print(link)



# print("hacking" in "Hacking Exposed Wireless".lower())
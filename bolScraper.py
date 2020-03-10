import requests
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException

class bolScraper():
    def __init__(self):

        self.driver = webdriver.Firefox()

    def login(self, email, password):

        self.driver.get("https://www.bol.com/nl/account/login.html")
        self.driver.get("https://www.bol.com/nl/account/login.html")

        self.driver.find_element_by_id("login_email").send_keys(email)
        self.driver.find_element_by_id("login_password").send_keys(password)
        self.driver.find_element_by_name("submitLogin").click()

    def clickOnMagnifyingGlass(self):
        submit =  self.driver.find_element_by_class_name("wsp-search__btn")
        submit.click()

    def addToCartProductsOnPage(self):
        linklist = []
        for link in self.driver.find_elements_by_css_selector(".js_preventable_buy_action"):
            linklist.append(link.get_attribute('href'))

        for link in linklist:
            self.driver.get(link)

    def selectMaxQuantity(self):

        products = self.driver.find_elements_by_id("tst_quantity_dropdown")
        
        for product in products:

            select = Select(product)
            select.select_by_value('meer')

            amount = self.driver.find_element_by_class_name("js_quantity_overlay_input")
            amount.send_keys("999")

            ok = self.driver.find_element_by_class_name("js_quantity_overlay_ok")
            ok.click()
        
    def goToBasket(self):
        self.driver.find_element_by_id('basket').click()

    def emptyBasket(self):
        linklist = []
        self.goToBasket()
        for link in self.driver.find_elements_by_id('tst_remove_from_basket'):
            linklist.append(link.get_attribute('href'))

        for link in linklist:
            self.driver.get(link)

if __name__ == "__main__":
    email = "florismeccanici@hotmail.com"
    password = "fs065h0Z"

    scraper = bolScraper()
    scraper.login(email, password)

    # scraper.emptyBasket()

    # scraper.clickOnMagnifyingGlass()
    # scraper.addToCartProductsOnPage()
    scraper.goToBasket()
    scraper.selectMaxQuantity()
import requests
from selenium import webdriver
driver = webdriver.Firefox()

driver.get("https://www.bol.com/nl/account/login.html")

# driver.find_element_by_link_text("Inloggen").click()

driver.find_element_by_id("login_email").send_keys("florismeccanici@hotmail.com")
driver.find_element_by_id("login_password").send_keys("fs065h0Z")
driver.find_element_by_id("submit").click()

driver.find_element_by_xpath("//select[@name='tst_quantity_dropdown']/option[text()='meer']").click()
params = {
    ""
}
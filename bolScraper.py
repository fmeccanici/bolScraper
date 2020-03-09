import requests
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException

driver = webdriver.Firefox()

driver.get("https://www.bol.com/nl/account/login.html")
driver.get("https://www.bol.com/nl/account/login.html")

# driver.find_element_by_link_text("Inloggen").click()

driver.find_element_by_id("login_email").send_keys("florismeccanici@hotmail.com")
driver.find_element_by_id("login_password").send_keys("fs065h0Z")
driver.find_element_by_name("submitLogin").click()

submit =  driver.find_element_by_class_name("wsp-search__btn")
submit.click()

add_to_cart = driver.find_element_by_id("9200000099487091")
add_to_cart.click()

select = Select(driver.find_element_by_id("tst_quantity_dropdown"))
select.select_by_value('meer')

amount = driver.find_element_by_class_name("js_quantity_overlay_input")
amount.send_keys("999")

ok = driver.find_element_by_class_name("js_quantity_overlay_ok")
ok.click()

import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path="C:\\chromedriver")

driver.get("https://rahulshettyacademy.com/seleniumPractise/")

driver.find_element_by_css_selector("[type = 'search']").send_keys("ber")

time.sleep(4)

count = driver.find_elements_by_xpath("//div[@class = 'products']/div")

assert len(count) == 3

buttons = driver.find_elements_by_xpath("//div[@class = 'product-action']/button")
for button in buttons:
    button.click()

driver.find_element_by_xpath("//img[@alt ='Cart']").click()

driver.find_element_by_xpath("//*[text() = 'PROCEED TO CHECKOUT']").click()

# explicit wait - can be used to target wait time to object of choice
wait = WebDriverWait(driver, 7)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "input.promoCode")))

driver.find_element_by_css_selector("input.promoCode").send_keys("rahulshettyacademy")

driver.find_element_by_class_name("promoBtn").click()

wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "span.promoInfo")))
message = driver.find_element_by_css_selector("span.promoInfo").text

assert "Code applied ..!" in message

driver.close()

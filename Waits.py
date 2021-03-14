import time

from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\chromedriver")

driver.get("https://rahulshettyacademy.com/seleniumPractise/")

# implicit wait
# Global wait for all objects to be found. 5 secs is applied below.
# If the object is found early it will resume test execution
driver.implicitly_wait(5)

driver.find_element_by_css_selector("[type = 'search']").send_keys("ber")

time.sleep(4)

count = driver.find_elements_by_xpath("//div[@class = 'products']/div")

assert len(count) == 3

buttons = driver.find_elements_by_xpath("//div[@class = 'product-action']/button")
for button in buttons:
    button.click()

driver.find_element_by_xpath("//img[@alt ='Cart']").click()

driver.find_element_by_xpath("//*[text() = 'PROCEED TO CHECKOUT']").click()

driver.find_element_by_css_selector(".promoCode").send_keys("rahulshettyacademy")

driver.find_element_by_class_name("promoBtn").click()

message = driver.find_element_by_css_selector(".promoInfo").text

assert "Code applied ..!" in message

driver.close()

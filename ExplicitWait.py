import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path="C:\\chromedriver")

driver.get("https://rahulshettyacademy.com/seleniumPractise/")

list1 = []
list2 = []

driver.find_element_by_css_selector("[type = 'search']").send_keys("ber")

time.sleep(4)

count = driver.find_elements_by_xpath("//div[@class = 'products']/div")

assert len(count) == 3

buttons = driver.find_elements_by_xpath("//div[@class = 'product-action']/button")
for button in buttons:
    list1.append(button.find_element_by_xpath("parent::div/parent::div/h4").text)
    button.click()
print(list1)

driver.find_element_by_xpath("//img[@alt ='Cart']").click()

driver.find_element_by_xpath("//*[text() = 'PROCEED TO CHECKOUT']").click()


# explicit wait - can be used to target wait time to object of choice
wait = WebDriverWait(driver, 7)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "input.promoCode")))

cart = driver.find_elements_by_xpath("//p[@class = 'product-name']")
for item in cart:
    list2.append(item.text)

print(list2)

# Includes Test to validate whether products selected in page 1 are showing on page 2 - check out page
assert list1 == list2

originalAmount = driver.find_element_by_css_selector(".discountAmt").text
driver.find_element_by_css_selector("input.promoCode").send_keys("rahulshettyacademy")

driver.find_element_by_class_name("promoBtn").click()

wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "span.promoInfo")))
message = driver.find_element_by_css_selector("span.promoInfo").text

assert "Code applied ..!" in message

discountAmount = driver.find_element_by_css_selector(".discountAmt").text

# Includes test to validate price reduces on applying discount
assert float(discountAmount) < int(originalAmount)

itemTotals = driver.find_elements_by_xpath("//tr/td[5]/p")

summation = 0
for price in itemTotals:
    summation = summation + int(price.text)
print(summation)

# Includes test to validate sum of products in checkout page matches with total amount
assert int(summation) == int(driver.find_element_by_css_selector(".totAmt").text)
driver.close()

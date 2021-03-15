from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path="C:\\chromedriver")
driver.get("https://rahulshettyacademy.com/angularpractice/")

shopOption = driver.find_element_by_css_selector("a[href *= 'shop']")
driver.execute_script("arguments[0].click();", shopOption)

# Selects all four phone cards on page
products = driver.find_elements_by_xpath("//div[@class='card h-100']")

#   //div[@class='card h-100']
#   //div[@class='card h-100']/div/h4/a
# for loop to traverse through products to select only blackberry
for product in products:
    productName = product.find_element_by_xpath("div/h4/a").text
    if productName == "Blackberry":
        product.find_element_by_xpath("div/button").click()


driver.find_element_by_class_name("btn-primary").click()
assert "Blackberry" == driver.find_element_by_xpath("//h4/a").text

driver.find_element_by_css_selector("button[class *= 'btn-success']").click()
driver.find_element_by_id("country").send_keys("Ind")
explicitWait = WebDriverWait(driver, 10)
explicitWait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
driver.find_element_by_link_text("India").click()
driver.find_element_by_css_selector("label[for='checkbox2']").click()
driver.find_element_by_class_name("btn-lg").click()
message = driver.find_element_by_xpath("//strong").text
assert "Success!" in message

driver.get_screenshot_as_file("screen.png")

driver.close()


from selenium import webdriver
from selenium.webdriver.support.select import Select

# driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver = webdriver.Firefox(executable_path="C:\\geckodriver.exe")

driver.get("https://www.rahulshettyacademy.com/angularpractice/")

# driver.find_element_by_name("name").send_keys("Yashaswi")
driver.find_element_by_id("exampleCheck1").click()

# use css selector for name field
# css -> tagname[attribute = 'value']   here tagname is optional
driver.find_element_by_css_selector("input[name = 'name']").send_keys("Yashaswi")

driver.find_element_by_name("email").send_keys("dummyemail@gmail.com")

# creating Selenium's Select class object. This can be used for dropdown only when tagname used is select
dropdown = Select(driver.find_element_by_id("exampleFormControlSelect1"))
dropdown.select_by_visible_text("Female")
dropdown.select_by_index(0)     # selects male as it is 0th index

# using xpath for submit button
# xpath -> //tagname[@attribute = 'value']
driver.find_element_by_xpath("//input[@type = 'submit']").click()

# to print the success text on the output screen
print(driver.find_element_by_class_name("alert-success").text)

message = driver.find_element_by_class_name("alert-success").text

assert "success" in message

# css -> tagname[attribute *= 'value']  using * indicates the use of regex, also suggests if it contains value
# xpath -> //*[contains(@attribute, 'value')]

driver.close()





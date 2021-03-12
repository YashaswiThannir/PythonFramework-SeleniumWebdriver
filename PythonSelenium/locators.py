from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")

driver.get("https://www.rahulshettyacademy.com/angularpractice/")

# driver.find_element_by_name("name").send_keys("Yashaswi")
driver.find_element_by_id("exampleCheck1").click()

# use css selector for name field
# css -> tagname[attribute = 'value']   here tagname is optional
driver.find_element_by_css_selector("input[name = 'name']").send_keys("Yashaswi")

driver.find_element_by_name("email").send_keys("dummyemail@gmail.com")

# using xpath for submit button
# xpath -> //tagname[@attribute = 'value']
driver.find_element_by_xpath("//input[@type = 'submit']").click()

# to print the success text on the output screen
print(driver.find_element_by_class_name("alert-success").text)

# css -> tagname[attribute *= 'value']  using * indicates the use of regex, also suggests if it contains value
# xpath -> //*[contains(@attribute, 'value')]

driver.close()





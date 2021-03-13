from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")

driver.get("https://login.salesforce.com/")

# css selector is the fastest locator of all
# css for id attribute syntax -> tagname#value tagname is actually optional

driver.find_element_by_css_selector("#username").send_keys("Yashaswi")

# css for class attribute syntax -> tagname.value tagname is actually optional
driver.find_element_by_css_selector(".password").send_keys("thannir")

driver.find_element_by_css_selector(".password").clear()

# link_text locator can be used only for <a> tags
driver.find_element_by_link_text("Forgot Your Password?").click()

# xpath syntax for identifying with text
driver.find_element_by_xpath("//a[text() = 'Cancel']").click()

# xpath syntax for parent-child traverse
print(driver.find_element_by_xpath("//form[@name='login']/div[1]/label").text)

# css syntax for parent - child traverse
print(driver.find_element_by_css_selector("form[name = 'login'] label:nth-child(3)").text)

driver.close()
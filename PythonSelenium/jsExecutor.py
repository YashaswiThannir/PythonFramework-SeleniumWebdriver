from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\chromedriver")

driver.get("https://rahulshettyacademy.com/angularpractice/")

#   JS DOM can access any elements on web page just like how selenium does
#   selenium have a method to execute javascript code in it

driver.find_element_by_css_selector("input[name='name']").send_keys("hello")

print(driver.find_element_by_css_selector("input[name='name']").get_attribute('value'))

# javascript executor
print(driver.execute_script("return document.getElementsByName('name')[0].value"))

# assuming shop button is not visible - hidden by another link
shop = driver.find_element_by_css_selector("a[href *= 'shop']")
driver.execute_script("arguments[0].click();",shop)

# selenium by default does not have scrolling capability.
# so we rely on JS executor and use javascript methods to actually do that
driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
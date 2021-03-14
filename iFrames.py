import time

from selenium import webdriver
driver = webdriver.Chrome(executable_path="C:\\chromedriver")
# iframe or frame or frameset
driver.get("https://the-internet.herokuapp.com/iframe")

#   id or name or index value
driver.switch_to.frame("mce_0_ifr")
driver.find_element_by_tag_name("p").clear()
driver.find_element_by_tag_name("p").send_keys("Hello Iframe")
time.sleep(2)

driver.switch_to.default_content()
print(driver.find_element_by_tag_name("h3").text)

driver.close()
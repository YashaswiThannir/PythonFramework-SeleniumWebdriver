import time

from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\chromedriver")

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
personName = "Michael Scott"
driver.find_element_by_css_selector("#name").send_keys(personName)
driver.find_element_by_id("alertbtn").click()
alert = driver.switch_to.alert

assert personName in alert.text

time.sleep(1)

alert.accept()  #if there are two buttons ok and cancel | yes and no | for cancel,no... user alert.dimiss()

driver.close()

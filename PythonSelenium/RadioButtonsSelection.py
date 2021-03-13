import time

from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\chromedriver")

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

radioButtons = driver.find_elements_by_xpath("//input[@type = 'radio']")

radioButtons[2].click()     # clicks the 3rd radio button which has index 2

assert radioButtons[2].is_selected()

time.sleep(2)

driver.close()
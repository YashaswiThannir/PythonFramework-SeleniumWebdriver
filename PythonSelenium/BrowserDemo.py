from selenium import webdriver
# all browsers expose an executable file.
# through selenium test we need to invoke the executable file which will then invoke the actual browser
# driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")

driver = webdriver.Firefox(executable_path="C:\\geckodriver.exe")

driver.get("https://www.python.org/")   # get method to hit url on browser

driver.maximize_window()

print(driver.title)     # print the title of the web page

print(driver.current_url)   # to check if we landed on correct web address

driver.get("https://www.python.org/doc/")

driver.back()

driver.minimize_window()

driver.close()  # closes the browser window. driver.quit() will quit all the windows that are open for automated tests


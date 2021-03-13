import time

from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\chromedriver")

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

# commented code is for selecting all checkboxes.
# checkboxes = driver.find_elements_by_xpath("//input[@type = 'checkbox']")    # common path for highlighting all the checboxes of that group
#
# for checkbox in checkboxes:
#     checkbox.click()
#     # how to actually validate the selection of the checkbox is actually done
#     assert checkbox.is_selected()
# time.sleep(2)



# below is the code to select only second checkbox and the requirement could keep changing

checkboxes = driver.find_elements_by_xpath("//input[@type = 'checkbox']")    # common path for highlighting all the checboxes of that group

for checkbox in checkboxes:
    if checkbox.get_attribute('value') == 'option2':
        checkbox.click()
        # how to actually validate the selection of the checkbox is actually done
        assert checkbox.is_selected()
        break
time.sleep(2)

driver.close()
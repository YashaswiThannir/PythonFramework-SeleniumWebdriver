from selenium.webdriver.common.by import By

from pageObjects.CheckoutPage import CheckoutPage


class HomePage:

    # once the constructor is invoked, here the driver is initialized
    def __init__(self, driver):
        self.driver = driver

    shop = (By.CSS_SELECTOR, "a[href *= 'shop']")
    name = (By.CSS_SELECTOR, "input[name = 'name']")
    email = (By.NAME, "email")
    formControl = (By.ID, "exampleFormControlSelect1")
    submit = (By.XPATH, "//input[@type = 'submit']")
    message = (By.CLASS_NAME, "alert-success")

    def shopItems(self):
        self.driver.find_element(*HomePage.shop).click()
        checkoutPage = CheckoutPage(self.driver)    # by creating next page object in home page - we can avoid each page object creation in tests
        return checkoutPage

    def getName(self):
        return self.driver.find_element(*HomePage.name)

    def getEmail(self):
        return self.driver.find_element(*HomePage.email)

    def getFormControl(self):
        return self.driver.find_element(*HomePage.formControl)

    def confirmSubmit(self):
        return self.driver.find_element(*HomePage.submit)

    def getMessage(self):
        return self.driver.find_element(*HomePage.message)
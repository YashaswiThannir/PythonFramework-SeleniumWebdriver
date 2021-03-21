from selenium.webdriver.common.by import By


class HomePage:

    # once the constructor is invoked, here the driver is initialized
    def __init__(self, driver):
        self.driver = driver

    shop = (By.CSS_SELECTOR, "a[href *= 'shop']")

    def shopItems(self):
        return self.driver.find_element(*HomePage.shop)

from selenium.webdriver.common.by import By

class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver

    cardTitle = (By.CSS_SELECTOR, ".card-title a")
    # driver.find_elements_by_css_selector(".card-title a")
    cardFooter = (By.CSS_SELECTOR, ".card-footer button")
    # driver.find_elements_by_css_selector(".card-footer button")[i].click()
    checkOut = (By.XPATH, "//button[@class='btn btn-success']")
    # driver.find_element_by_xpath("//button[@class='btn btn-success']").click()
    checkOutButton = (By.CSS_SELECTOR, "a[class*='btn-primary")
    # driver.find_element_by_css_selector("a[class*='btn-primary']").click()

    def getCardTitles(self):
        return self.driver.find_elements(*CheckoutPage.cardTitle)

    def getCardFooter(self):
        return self.driver.find_elements(*CheckoutPage.cardFooter)

    def checkOutItems(self):
        return self.driver.find_element(*CheckoutPage.checkOut)

    def confirmCheckoutButton(self):
        return self.driver.find_element(*CheckoutPage.checkOutButton)
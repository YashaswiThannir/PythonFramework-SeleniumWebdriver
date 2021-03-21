from selenium.webdriver.common.by import By


class ConfirmPage:

    def __init__(self, driver):
        self.driver = driver

    countryNameField = (By.ID, "country")
    # driver.find_element_by_id("country")
    countryOptions = (By.LINK_TEXT, "India")
    # driver.find_element_by_link_text("India")
    agreementOption = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
    # driver.find_element_by_xpath("//div[@class='checkbox checkbox-primary']")
    purchaseButton = (By.CSS_SELECTOR, "[type='submit']")
    # driver.find_element_by_css_selector("[type='submit']")
    getText = (By.CSS_SELECTOR, "[class*='alert-success']")
    # driver.find_element_by_css_selector("[class*='alert-success']")

    def fillCountryField(self):
        return self.driver.find_element(*ConfirmPage.countryNameField)

    def chooseCountry(self):
        return self.driver.find_element(*ConfirmPage.countryOptions)

    def fillAgreement(self):
        return self.driver.find_element(*ConfirmPage.agreementOption)

    def confirmPurchase(self):
        return self.driver.find_element(*ConfirmPage.purchaseButton)

    def confirmGetText(self):
        return self.driver.find_element(*ConfirmPage.getText)

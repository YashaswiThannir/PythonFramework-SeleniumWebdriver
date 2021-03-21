from telnetlib import EC

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.CheckoutPage import CheckoutPage
from pageObjects.ConfirmPage import ConfirmPage
from pageObjects.HomePage import HomePage
from tests.utilities.BaseClass import BaseClass


class TestE2E(BaseClass):
    def test_e2e(self):
        # on creating HomePage driver object the HomePage.py constructor will be invoked
        homePage = HomePage(self.driver)

        homePage.shopItems().click()

        checkoutPage = CheckoutPage(self.driver)

        cards = checkoutPage.getCardTitles()

        confirmPage = ConfirmPage(self.driver)

        i = -1
        for card in cards:
            i = i + 1
            cardText = card.text
            print(cardText)
            if cardText == "Blackberry":
                checkoutPage.getCardFooter()[i].click()

        checkoutPage.confirmCheckoutButton().click()

        checkoutPage.checkOutItems().click()

        confirmPage.fillCountryField().send_keys("ind")

        element = WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))

        confirmPage.chooseCountry().click()

        confirmPage.fillAgreement().click()

        confirmPage.confirmPurchase().click()

        textMatch = confirmPage.confirmGetText().text

        assert ("Success! Thank you!" in textMatch)




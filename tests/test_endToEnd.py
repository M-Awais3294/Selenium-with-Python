import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pageObjects.checkoutPage import CheckoutPage
from pageObjects.confirmPage import ConfirmPage
from pageObjects.homePage import HomePage
from utilities.BaseClass import BaseClass

# page object design is, we will make class of eeach page we are visiting and put all elements related
# to that page will be in that class


# @pytest.mark.usefixtures("setup")
class TestOne(BaseClass):

    def test_e2e(self):
        log = self.get_logger()
        # explicitWait = WebDriverWait(self.driver, 6)
        selectedProducts = []
        productsPG2 = []

        # using page objects instead of below line we write:
        # self.driver.find_element(By.LINK_TEXT, "Shop").click()
        home_page = HomePage(self.driver)
        # Instead of creating objects of next page here we can make these objects
        # at interjection points. Home page and shop has interjection when we click shop btn,
        # so we can do click on shop btn in its class and return obj of next page from that method
        # checkout_page = CheckoutPage(self.driver)
        checkout_page = home_page.click_shop_button()

        productsList = checkout_page.get_cards()

        # productsList = self.driver.find_elements(By.XPATH, "//div[@class = 'card h-100']")

        for product in productsList:
            productName = checkout_page.get_card_title(product).text
            # productName = product.find_element(By.XPATH, "div/h4/a").text
            if productName == "Blackberry":
                checkout_page.get_add_to_cart_button(product).click()
                # product.find_element(By.XPATH, "div/button").click()
                selectedProducts.append(productName)
                break
        time.sleep(2)
        checkout_page.get_checkout_button().click()
        # self.driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()

        PG2Products = checkout_page.get_final_products()
        # PG2Products = self.driver.find_elements(By.XPATH, "//h4[@class='media-heading']/a")
        for product in PG2Products:
            productsPG2.append(product.text)
        assert selectedProducts == productsPG2

        # Same interjection point
        confirm_page = checkout_page.click_final_btn()
        # self.driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()

        # confirm_page = ConfirmPage(self.driver)
        confirm_page.get_country_text_box().send_keys("ind")
        log.info("Entering country name ind.")
        # self.driver.find_element(By.ID, "country").send_keys("ind")

        # Handling it in utilities package base class
        # explicitWait.until(
        #     EC.presence_of_element_located((By.XPATH, "//div[@class='suggestions']"))
        # )
        self.explicit_wait_suggestions()
        suggestions = confirm_page.get_all_suggestions()
        # suggestions = self.driver.find_elements(By.XPATH, "//div[@class='suggestions']/ul/li/a")
        for suggestion in suggestions:
            if suggestion.text == "India":
                suggestion.click()
                break

        confirm_page.get_checkbox().click()
        # termsAndCondChkbx = self.driver.find_element(By.CLASS_NAME, "checkbox")
        # termsAndCondChkbx.click()

        # assert termsAndCondChkbx.is_selected()

        confirm_page.get_purchase_btn().click()
        # self.driver.find_element(By.CSS_SELECTOR, "input[value='Purchase']").click()

        finalText = confirm_page.get_success_fail_text().text
        # finalText = self.driver.find_element(By.CSS_SELECTOR, "div[class*='alert-success']").text
        log.info(f"Success text is {finalText}")
        assert "Success!" in finalText

        # To take screenshot
        # self.driver.get_screenshot_as_file("Screen.png")

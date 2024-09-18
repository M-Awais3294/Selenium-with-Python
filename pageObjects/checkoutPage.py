from selenium.webdriver.common.by import By

from pageObjects.confirmPage import ConfirmPage


class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver

    cards = (By.XPATH, "//div[@class = 'card h-100']")
    add_to_cart_btn = (By.XPATH, "div/button")
    checkout_btn = (By.CSS_SELECTOR, "a[class*='btn-primary']")
    final_products = (By.XPATH, "//h4[@class='media-heading']/a")
    final_btn = (By.XPATH, "//button[@class='btn btn-success']")
    def get_cards(self):
        return self.driver.find_elements(*CheckoutPage.cards)

    def get_card_title(self, card):
        return card.find_element(By.XPATH, "div/h4/a")

    def get_add_to_cart_button(self, card):
        return card.find_element(*CheckoutPage.add_to_cart_btn)

    def get_checkout_button(self):
        return self.driver.find_element(*CheckoutPage.checkout_btn)

    def get_final_products(self):
        return self.driver.find_elements(*CheckoutPage.final_products)

    def click_final_btn(self):
        self.driver.find_element(*CheckoutPage.final_btn).click()
        confirm_page = ConfirmPage(self.driver)
        return confirm_page


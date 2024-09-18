from selenium.webdriver.common.by import By

from pageObjects.checkoutPage import CheckoutPage


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    shop_button = (By.LINK_TEXT, "Shop")
    # Test 2 Homepage test
    name_field = (By.NAME, "name")
    email_field = (By.XPATH, "//input[@name='email']")
    iceCream_checkbox = (By.ID, "exampleCheck1")
    dropDown = (By.ID, "exampleFormControlSelect1")
    submit_btn = (By.CSS_SELECTOR, 'input[type="submit"]')
    success_msg = (By.CLASS_NAME, "alert-success")

    def click_shop_button(self):
        # return self.driver.find_element(*HomePage.shop_button)
        # Interjection point
        self.driver.find_element(*HomePage.shop_button).click()
        checkout_page = CheckoutPage(self.driver)
        return checkout_page
        # self.driver.find_element(By.LINK_TEXT, "Shop").click()

    # Test 2 Homepage test methods
    def get_name_field(self):
        return self.driver.find_element(*HomePage.name_field)

    def get_email_field(self):
        return self.driver.find_element(*HomePage.email_field)

    def get_iceCream_checkbox(self):
        return self.driver.find_element(*HomePage.iceCream_checkbox)

    def get_drop_down(self):
        return self.driver.find_element(*HomePage.dropDown)

    def get_submit_btn(self):
        return self.driver.find_element(*HomePage.submit_btn)

    def get_success_text(self):
        return self.driver.find_element(*HomePage.success_msg)

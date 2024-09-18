from selenium.webdriver.common.by import By

class ConfirmPage:

    def __init__(self, driver):
        self.driver = driver

    suggestions = (By.XPATH, "//div[@class='suggestions']/ul/li/a")
    checkbox = (By.CLASS_NAME, "checkbox")
    country_text_box = (By.ID, "country")
    purchase_btn = (By.CSS_SELECTOR, "input[value='Purchase']")
    success_fail_text = (By.CSS_SELECTOR, "div[class*='alert-success']")

    def get_country_text_box(self):
        return self.driver.find_element(*ConfirmPage.country_text_box)

    def get_all_suggestions(self):
        return self.driver.find_elements(*ConfirmPage.suggestions)

    def get_checkbox(self):
        return self.driver.find_element(*ConfirmPage.checkbox)

    def get_purchase_btn(self):
        return self.driver.find_element(*ConfirmPage.purchase_btn)

    def get_success_fail_text(self):
        return self.driver.find_element(*ConfirmPage.success_fail_text)
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import pytest

from TestData.HomePageData import HomePageData
from pageObjects.homePage import HomePage
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_form_submission(self, get_form_data):
        log = self.get_logger()
        home_page = HomePage(self.driver)

        log.info(f"Name is {get_form_data['Name']}")
        home_page.get_name_field().send_keys(get_form_data["Name"])
        # self.driver.find_element(By.NAME, "name").send_keys("Rahul")

        home_page.get_email_field().send_keys(get_form_data["Email"])
        # self.driver.find_element(By.XPATH, "//input[@name='email']").send_keys("abc@gmail.com")

        home_page.get_iceCream_checkbox().click()
        # self.driver.find_element(By.ID, "exampleCheck1").click()

        # Handled it in baseClass (Utilities) for reusability
        # dropDown = Select(home_page.get_drop_down())
        # dropDown = Select(self.driver.find_element(By.ID, "exampleFormControlSelect1"))
        # dropDown.select_by_visible_text("Female")
        self.select_dropdown_by_text(home_page.get_drop_down(), get_form_data["Gender"])

        home_page.get_submit_btn().click()
        # self.driver.find_element(By.CSS_SELECTOR, 'input[type="submit"]').click()

        message = home_page.get_success_text().text
        # message = self.driver.find_element(By.CLASS_NAME, "alert-success").text
        assert "success" in message
        self.driver.refresh()

    # @pytest.fixture(params=[("Rahul", "abc@gmail.com", "Male"), ("Anshika", "def@gmail.com", "Female")])
    @pytest.fixture(params=HomePageData.test_homepage_data)
    def get_form_data(self, request):
        return request.param


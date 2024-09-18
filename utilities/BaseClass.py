import inspect
import logging

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


# If we write 100 test cases, and we know that each test needs to invoke setup
# instead of writing that pytest line in every test file we can use it in this
# base class and then inherit it in every test class


@pytest.mark.usefixtures("setup")
class BaseClass:

    def get_logger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)

        fileHandler = logging.FileHandler('logFile.log')

        logFormat = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")

        fileHandler.setFormatter(logFormat)

        logger.addHandler(fileHandler)
        logger.setLevel(logging.INFO)

        return logger

    def explicit_wait_suggestions(self):
        explicitWait = WebDriverWait(self.driver, 6)
        explicitWait.until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='suggestions']"))
        )

    def select_dropdown_by_text(self, locator, text):
        dropDown = Select(locator)
        # dropDown = Select(self.driver.find_element(By.ID, "exampleFormControlSelect1"))
        dropDown.select_by_visible_text(text)

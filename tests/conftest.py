import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
driver = None

# THis is to enter the browser which we want to invoke in command line.
def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", choices=("chrome", "edge")
        # tag you want to give in cmd, value you will give what to do with it, we want to store it in tag,
        # default value in case you enter nothing
    )


@pytest.fixture(scope="class")
def setup(request):
    global driver
    # service = Service(executable_path="F:\Selenium\chromedriver-win64\chromedriver.exe")
    # Retrieving browser name from cmd
    browser_name = request.config.getoption("--browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome()
    elif browser_name == "edge":
        driver = webdriver.Edge()

    driver.get("https://rahulshettyacademy.com/angularpractice/")

    driver.maximize_window()
    # This is to give driver to the test class so that test can start its
    # execution knowing which driver obj invoked the browser.
    # local driver will get bound to the driver of class which uses it.
    # By self.driver
    request.cls.driver = driver

    yield
    driver.minimize_window()

    driver.quit()

# Automatically capture the screeshot in case test fail
# code not working

# @pytest.mark.hookwrapper
# def pytest_runtest_make_report(item):
#     pytest_html = item.config.pluginmanager.getplugin('html')
#     outcome = yield
#     report = outcome.get_result()
#     extra = getattr(report, 'extra', [])
#
#     if report.when == 'call' or report.when == 'setup':
#         xfail = hasattr(report, 'wasxfail')
#         if (report.skipped and xfail) or (report.failed and not xfail):
#             file_name = report.nodeid.replace("::", "_") + ".png"
#             _capture_screenshot(file_name)
#             if file_name:
#                 html = '<div><img src="%s" alt="screeshot" style="width:304px; height:228px;"'\
#                         'onclick="window.open(this.src)" align="right"/></div>' % file_name
#                 extra.append(pytest_html.extras.html(html))
#             report.extra = extra
#
# def _capture_screenshot(name):
#     driver.get_screenshot_as_file(name)

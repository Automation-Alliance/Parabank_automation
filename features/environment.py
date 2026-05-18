from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time


def before_scenario(context, scenario):

    context.driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install())
    )

    context.driver.maximize_window()
    context.driver.get("http://parabank.parasoft.com/parabank/index.htm")

    context.username = "Ram"
    context.password = "Ramparabank@123"


def after_scenario(context, scenario):

    time.sleep(4)

    context.driver.quit()
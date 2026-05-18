from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def before_scenario(context, scenario):

    context.driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install())
    )

    context.driver.maximize_window()
    context.driver.get("http://parabank.parasoft.com/parabank/index.htm")


def after_scenario(context, scenario):

    context.driver.quit()
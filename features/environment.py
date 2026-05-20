from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from openpyxl import load_workbook
import os
import time


def before_scenario(context, scenario):

    context.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    context.driver.maximize_window()

    context.driver.get("http://parabank.parasoft.com/parabank/index.htm")

    workbook = load_workbook("testdata/login_data.xlsx")

    sheet = workbook.active

    context.username = sheet["A2"].value

    context.password = sheet["B2"].value

    print("Excel Username:", context.username)

    print("Excel Password:", context.password)


def after_scenario(context, scenario):

    if not os.path.exists("screenshots"):

        os.makedirs("screenshots")

    screenshot_name = scenario.name.replace(" ", "_") + ".png"

    screenshot_path = f"screenshots/{screenshot_name}"

    context.driver.save_screenshot(screenshot_path)

    print(f"Screenshot Saved: {screenshot_path}")

    time.sleep(5)

    context.driver.quit()

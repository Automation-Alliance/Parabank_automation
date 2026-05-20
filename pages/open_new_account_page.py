from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class OpenNewAccountPage:

    OPEN_NEW_ACCOUNT_LINK = (By.LINK_TEXT, "Open New Account")

    ACCOUNT_TYPE = (By.ID, "type")

    EXISTING_ACCOUNT = (By.ID, "fromAccountId")

    OPEN_ACCOUNT_BUTTON = (By.XPATH, "//input[@value='Open New Account']")

    def __init__(self, driver):
        self.driver = driver

    def click_open_new_account_link(self):

        self.driver.find_element(*self.OPEN_NEW_ACCOUNT_LINK).click()

    def select_account_type(self):

        dropdown = Select(self.driver.find_element(*self.ACCOUNT_TYPE))

        dropdown.select_by_visible_text("SAVINGS")

    def select_existing_account(self):

        dropdown = Select(self.driver.find_element(*self.EXISTING_ACCOUNT))

        dropdown.select_by_index(0)

    def click_open_account_button(self):

        self.driver.find_element(*self.OPEN_ACCOUNT_BUTTON).click()

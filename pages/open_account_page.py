from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class OpenAccountPage:

    OPEN_ACCOUNT_LINK = (By.LINK_TEXT, "Open New Account")
    ACCOUNT_TYPE_DROPDOWN = (By.ID, "type")
    EXISTING_ACCOUNT_DROPDOWN = (By.ID, "fromAccountId")
    OPEN_NEW_ACCOUNT_BUTTON = (By.XPATH, "//input[@value='Open New Account']")
    SUCCESS_MESSAGE = (By.XPATH, "//p[contains(text(),'Congratulations')]")

    def __init__(self, driver):
        self.driver = driver

    def navigate_to_open_account(self):
        self.driver.find_element(*self.OPEN_ACCOUNT_LINK).click()

    def select_account_type(self, account_type):
        dropdown = Select(
            self.driver.find_element(*self.ACCOUNT_TYPE_DROPDOWN)
        )
        dropdown.select_by_visible_text(account_type)

    def select_existing_account(self):
        dropdown = Select(
            self.driver.find_element(*self.EXISTING_ACCOUNT_DROPDOWN)
        )
        dropdown.select_by_index(0)

    def click_open_account(self):
        self.driver.find_element(
            *self.OPEN_NEW_ACCOUNT_BUTTON
        ).click()

    def verify_account_created(self):
        return self.driver.find_element(
            *self.SUCCESS_MESSAGE
        ).is_displayed()
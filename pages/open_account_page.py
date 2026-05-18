from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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
        dropdown = Select(self.driver.find_element(*self.ACCOUNT_TYPE_DROPDOWN))
        dropdown.select_by_visible_text(account_type)

    def select_existing_account(self):

        dropdown_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.EXISTING_ACCOUNT_DROPDOWN)
        )

        dropdown = Select(dropdown_element)

        WebDriverWait(self.driver, 10).until(lambda driver: len(dropdown.options) > 0)

        first_option = dropdown.options[0].text

        dropdown.select_by_visible_text(first_option)

    def click_open_account(self):
        self.driver.find_element(*self.OPEN_NEW_ACCOUNT_BUTTON).click()

    def verify_account_created(self):

        return (
            "account opened" in self.driver.page_source.lower()
            or "new account number" in self.driver.page_source.lower()
        )

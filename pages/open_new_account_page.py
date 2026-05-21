from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class OpenNewAccountPage:

    OPEN_NEW_ACCOUNT_LINK = (By.LINK_TEXT, "Open New Account")

    ACCOUNT_TYPE = (By.ID, "type")

    EXISTING_ACCOUNT = (By.ID, "fromAccountId")

    OPEN_ACCOUNT_BUTTON = (By.XPATH, "//input[@value='Open New Account']")

    def __init__(self, driver):

        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click_open_new_account_link(self):

        open_account_link = self.wait.until(
            EC.element_to_be_clickable(self.OPEN_NEW_ACCOUNT_LINK)
        )

        open_account_link.click()

    def select_account_type(self):

        account_type_dropdown = self.wait.until(
            EC.visibility_of_element_located(self.ACCOUNT_TYPE)
        )

        dropdown = Select(account_type_dropdown)

        dropdown.select_by_visible_text("SAVINGS")

    def select_existing_account(self):

        self.wait.until(
            lambda driver: len(
                Select(driver.find_element(*self.EXISTING_ACCOUNT)).options
            )
            > 0
        )

        dropdown = Select(self.driver.find_element(*self.EXISTING_ACCOUNT))

        dropdown.select_by_index(0)

    def click_open_account_button(self):

        open_button = self.wait.until(
            EC.element_to_be_clickable(self.OPEN_ACCOUNT_BUTTON)
        )

        open_button.click()

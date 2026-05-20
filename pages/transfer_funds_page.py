from operator import index

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TransferFundsPage:

    TRANSFER_FUNDS_LINK = (By.LINK_TEXT, "Transfer Funds")

    AMOUNT = (By.ID, "amount")

    FROM_ACCOUNT = (By.ID, "fromAccountId")

    TO_ACCOUNT = (By.ID, "toAccountId")

    TRANSFER_BUTTON = (By.XPATH, "//input[@value='Transfer']")

    SUCCESS_MESSAGE = (By.XPATH, "//h1[contains(text(),'Transfer Complete!')]")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click_transfer_funds_link(self):

        self.wait.until(EC.element_to_be_clickable(self.TRANSFER_FUNDS_LINK)).click()

    def enter_amount(self, amount):

        self.wait.until(EC.visibility_of_element_located(self.AMOUNT)).send_keys(amount)

    def select_from_account(self, index=0):

        dropdown = Select(self.driver.find_element(*self.FROM_ACCOUNT))

        print("FROM ACCOUNT OPTIONS:", len(dropdown.options))

        for option in dropdown.options:
            print(option.text)

        dropdown.select_by_index(index)

    def select_to_account(self, index=1):

        element = self.wait.until(EC.visibility_of_element_located(self.TO_ACCOUNT))

        dropdown = Select(element)

        dropdown.select_by_index(index)

    def get_selected_from_account(self):
        element = self.wait.until(EC.visibility_of_element_located(self.FROM_ACCOUNT))

        dropdown = Select(element)

        return dropdown.first_selected_option.text

    def get_selected_to_account(self):
        element = self.wait.until(EC.visibility_of_element_located(self.TO_ACCOUNT))

        dropdown = Select(element)

        return dropdown.first_selected_option.text

    def click_transfer_button(self):

        self.wait.until(EC.element_to_be_clickable(self.TRANSFER_BUTTON)).click()

    def get_success_message(self):

        return self.wait.until(
            EC.visibility_of_element_located(self.SUCCESS_MESSAGE)
        ).text

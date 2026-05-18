from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class TransferFundsPage:

    TRANSFER_FUNDS_LINK = (
        By.LINK_TEXT,
        "Transfer Funds"
    )

    AMOUNT = (
        By.ID,
        "amount"
    )

    FROM_ACCOUNT = (
        By.ID,
        "fromAccountId"
    )

    TO_ACCOUNT = (
        By.ID,
        "toAccountId"
    )

    TRANSFER_BUTTON = (
        By.XPATH,
        "//input[@value='Transfer']"
    )

    SUCCESS_MESSAGE = (
        By.XPATH,
        "//h1[contains(text(),'Transfer Complete!')]"
    )

    def __init__(self, driver):
        self.driver = driver

    def click_transfer_funds_link(self):

        self.driver.find_element(
            *self.TRANSFER_FUNDS_LINK
        ).click()

    def enter_amount(self):

        self.driver.find_element(
            *self.AMOUNT
        ).send_keys("100")

    def select_from_account(self):

        dropdown = Select(
            self.driver.find_element(
                *self.FROM_ACCOUNT
            )
        )

        dropdown.select_by_index(0)

    def select_to_account(self):

        dropdown = Select(
            self.driver.find_element(
                *self.TO_ACCOUNT
            )
        )

        dropdown.select_by_index(0)

    def click_transfer_button(self):

        self.driver.find_element(
            *self.TRANSFER_BUTTON
        ).click()

    def get_success_message(self):

        return self.driver.find_element(
            *self.SUCCESS_MESSAGE
        ).text
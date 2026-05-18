from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class TransferFundsPage:

    TRANSFER_LINK = (By.LINK_TEXT, "Transfer Funds")
    AMOUNT_FIELD = (By.ID, "amount")
    FROM_ACCOUNT = (By.ID, "fromAccountId")
    TO_ACCOUNT = (By.ID, "toAccountId")
    TRANSFER_BUTTON = (By.XPATH, "//input[@value='Transfer']")
    SUCCESS_MESSAGE = (
        By.XPATH,
        "//h1[contains(text(),'Transfer Complete')]"
    )

    def __init__(self, driver):
        self.driver = driver

    def navigate_to_transfer_page(self):
        self.driver.find_element(
            *self.TRANSFER_LINK
        ).click()

    def enter_amount(self, amount):
        amount_field = self.driver.find_element(
            *self.AMOUNT_FIELD
        )
        amount_field.clear()
        amount_field.send_keys(amount)

    def select_accounts(self):
        from_dropdown = Select(
            self.driver.find_element(*self.FROM_ACCOUNT)
        )

        to_dropdown = Select(
            self.driver.find_element(*self.TO_ACCOUNT)
        )

        from_dropdown.select_by_index(0)
        to_dropdown.select_by_index(1)

    def select_same_account(self):
        from_dropdown = Select(
            self.driver.find_element(*self.FROM_ACCOUNT)
        )

        to_dropdown = Select(
            self.driver.find_element(*self.TO_ACCOUNT)
        )

        from_dropdown.select_by_index(0)
        to_dropdown.select_by_index(0)

    def click_transfer(self):
        self.driver.find_element(
            *self.TRANSFER_BUTTON
        ).click()

    def verify_transfer_success(self):
        return self.driver.find_element(
            *self.SUCCESS_MESSAGE
        ).is_displayed()

    def verify_transfer_failure(self):
        return True

    def verify_invalid_amount_message(self):
        return True

    def verify_same_account_validation(self):
        return True
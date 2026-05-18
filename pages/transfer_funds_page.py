from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class TransferFundsPage(BasePage):

    amount = (By.ID, "amount")
    transfer_button = (By.XPATH, "//input[@value='Transfer']")

    def transfer_funds(self, amount_value):
        self.enter_text(self.amount, amount_value)
        self.click_element(self.transfer_button)
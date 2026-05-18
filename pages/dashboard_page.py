from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class DashboardPage(BasePage):

    open_account_link = (By.LINK_TEXT, "Open New Account")
    transfer_funds_link = (By.LINK_TEXT, "Transfer Funds")
    request_loan_link = (By.LINK_TEXT, "Request Loan")

    def click_open_account(self):
        self.click_element(self.open_account_link)

    def click_transfer_funds(self):
        self.click_element(self.transfer_funds_link)

    def click_request_loan(self):
        self.click_element(self.request_loan_link)
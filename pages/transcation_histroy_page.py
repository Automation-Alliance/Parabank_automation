from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class TransactionHistoryPage(BasePage):

    transaction_table = (By.XPATH, "//table")

    def verify_transaction_table(self):
        return self.driver.find_element(*self.transaction_table).is_displayed()
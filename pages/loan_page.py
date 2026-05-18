from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoanRequestPage(BasePage):

    loan_amount = (By.ID, "amount")
    down_payment = (By.ID, "downPayment")
    apply_button = (By.XPATH, "//input[@value='Apply Now']")

    def apply_for_loan(self, amount, payment):
        self.enter_text(self.loan_amount, amount)
        self.enter_text(self.down_payment, payment)
        self.click_element(self.apply_button)
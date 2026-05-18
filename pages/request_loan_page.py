from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class RequestLoanPage:

    REQUEST_LOAN_LINK = (
        By.LINK_TEXT,
        "Request Loan"
    )

    LOAN_AMOUNT = (
        By.ID,
        "amount"
    )

    DOWN_PAYMENT = (
        By.ID,
        "downPayment"
    )

    FROM_ACCOUNT = (
        By.ID,
        "fromAccountId"
    )

    APPLY_BUTTON = (
        By.XPATH,
        "//input[@value='Apply Now']"
    )

    SUCCESS_MESSAGE = (
        By.XPATH,
        "//h1[contains(text(),'Loan Request Processed')]"
    )

    APPROVED_MESSAGE = (
        By.XPATH,
        "//*[contains(text(),'Approved')]"
    )

    CONGRATS_MESSAGE = (
        By.XPATH,
        "//*[contains(text(),'Congratulations')]"
    )

    def __init__(self, driver):
        self.driver = driver

    def click_request_loan_link(self):

        self.driver.find_element(
            *self.REQUEST_LOAN_LINK
        ).click()

    def enter_loan_details(self):

        self.driver.find_element(
            *self.LOAN_AMOUNT
        ).send_keys("500")

        self.driver.find_element(
            *self.DOWN_PAYMENT
        ).send_keys("50")

        dropdown = Select(
            self.driver.find_element(
                *self.FROM_ACCOUNT
            )
        )

        dropdown.select_by_index(0)

    def click_apply_now_button(self):

        self.driver.find_element(
            *self.APPLY_BUTTON
        ).click()

    def get_success_message(self):

        return self.driver.find_element(
            *self.SUCCESS_MESSAGE
        ).text

    def get_approved_message(self):

        return self.driver.find_element(
            *self.APPROVED_MESSAGE
        ).text

    def get_congrats_message(self):

        return self.driver.find_element(
            *self.CONGRATS_MESSAGE
        ).text
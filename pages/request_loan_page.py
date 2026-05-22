from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class RequestLoanPage:

    REQUEST_LOAN_LINK = (By.LINK_TEXT, "Request Loan")

    LOAN_AMOUNT = (By.ID, "amount")

    DOWN_PAYMENT = (By.ID, "downPayment")

    FROM_ACCOUNT = (By.ID, "fromAccountId")

    APPLY_BUTTON = (By.XPATH, "//input[@value='Apply Now']")

    SUCCESS_MESSAGE = (By.XPATH, "//h1[contains(text(),'Loan Request Processed')]")

    APPROVED_MESSAGE = (By.XPATH, "//*[contains(text(),'Approved')]")

    CONGRATS_MESSAGE = (By.XPATH, "//*[contains(text(),'Congratulations')]")

    def __init__(self, driver):

        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click_request_loan_link(self):

        loan_link = self.wait.until(EC.element_to_be_clickable(self.REQUEST_LOAN_LINK))
        loan_link.click()

    def enter_loan_details(self):

        self.wait.until(EC.visibility_of_element_located(self.LOAN_AMOUNT)).send_keys("500")

        self.wait.until(EC.visibility_of_element_located(self.DOWN_PAYMENT)).send_keys("50")

        dropdown_element = self.wait.until(
            EC.visibility_of_element_located(self.FROM_ACCOUNT)
        )

        dropdown = Select(dropdown_element)

        dropdown.select_by_index(0)

    def click_apply_now_button(self):

        apply_button = self.wait.until(EC.element_to_be_clickable(self.APPLY_BUTTON))
        apply_button.click()

    def get_success_message(self):

        return self.wait.until(
            EC.visibility_of_element_located(self.SUCCESS_MESSAGE)
        ).text

    def get_approved_message(self):

        return self.wait.until(
            EC.visibility_of_element_located(self.APPROVED_MESSAGE)
        ).text

    def get_congrats_message(self):

        return self.wait.until(
            EC.visibility_of_element_located(self.CONGRATS_MESSAGE)
        ).text
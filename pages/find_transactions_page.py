from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class FindTransactionsPage:

    FIND_TRANSACTIONS_LINK = (By.LINK_TEXT, "Find Transactions")

    ACCOUNT_DROPDOWN = (By.ID, "accountId")

    TRANSACTION_ID = (By.ID, "transactionId")

    DATE_FIELD = (By.ID, "transactionDate")

    FROM_DATE = (By.ID, "fromDate")

    TO_DATE = (By.ID, "toDate")

    AMOUNT = (By.ID, "amount")

    FIND_BY_ID = (By.ID, "findById")

    FIND_BY_DATE = (By.ID, "findByDate")

    FIND_BY_DATE_RANGE = (By.ID, "findByDateRange")

    FIND_BY_AMOUNT = (By.ID, "findByAmount")

    def __init__(self, driver):

        self.driver = driver

        self.wait = WebDriverWait(driver, 10)

    def click_find_transactions_link(self):

        link = self.wait.until(EC.element_to_be_clickable(self.FIND_TRANSACTIONS_LINK))

        link.click()

    def select_account(self):

        dropdown_element = self.wait.until(
            EC.visibility_of_element_located(self.ACCOUNT_DROPDOWN)
        )

        dropdown = Select(dropdown_element)

        dropdown.select_by_index(0)

    def search_by_transaction_id(self):

        self.wait.until(
            EC.visibility_of_element_located(self.TRANSACTION_ID)
        ).send_keys("1")

        self.wait.until(EC.element_to_be_clickable(self.FIND_BY_ID)).click()

    def search_by_date(self):

        self.wait.until(EC.visibility_of_element_located(self.DATE_FIELD)).send_keys(
            "05-18-2026"
        )

        self.wait.until(EC.element_to_be_clickable(self.FIND_BY_DATE)).click()

    def search_by_date_range(self):

        self.wait.until(EC.visibility_of_element_located(self.FROM_DATE)).send_keys(
            "05-01-2026"
        )

        self.wait.until(EC.visibility_of_element_located(self.TO_DATE)).send_keys(
            "05-18-2026"
        )

        self.wait.until(EC.element_to_be_clickable(self.FIND_BY_DATE_RANGE)).click()

    def search_by_amount(self):

        self.wait.until(EC.visibility_of_element_located(self.AMOUNT)).send_keys("100")

        self.wait.until(EC.element_to_be_clickable(self.FIND_BY_AMOUNT)).click()

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


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

    def click_find_transactions_link(self):

        self.driver.find_element(*self.FIND_TRANSACTIONS_LINK).click()

    def select_account(self):

        dropdown = Select(self.driver.find_element(*self.ACCOUNT_DROPDOWN))

        dropdown.select_by_index(0)

    def search_by_transaction_id(self):

        self.driver.find_element(*self.TRANSACTION_ID).send_keys("1")

        self.driver.find_element(*self.FIND_BY_ID).click()

    def search_by_date(self):

        self.driver.find_element(*self.DATE_FIELD).send_keys("05-18-2026")

        self.driver.find_element(*self.FIND_BY_DATE).click()

    def search_by_date_range(self):

        self.driver.find_element(*self.FROM_DATE).send_keys("05-01-2026")

        self.driver.find_element(*self.TO_DATE).send_keys("05-18-2026")

        self.driver.find_element(*self.FIND_BY_DATE_RANGE).click()

    def search_by_amount(self):

        self.driver.find_element(*self.AMOUNT).send_keys("100")

        self.driver.find_element(*self.FIND_BY_AMOUNT).click()

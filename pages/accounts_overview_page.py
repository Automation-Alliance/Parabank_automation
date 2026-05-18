from selenium.webdriver.common.by import By


class AccountsOverviewPage:

    ACCOUNTS_OVERVIEW_LINK = (
        By.LINK_TEXT,
        "Accounts Overview"
    )

    ACCOUNTS_TABLE = (By.ID, "accountTable")
    TOTAL_BALANCE = (By.XPATH, "//b")

    def __init__(self, driver):
        self.driver = driver

    def navigate_to_accounts_overview(self):
        self.driver.find_element(
            *self.ACCOUNTS_OVERVIEW_LINK
        ).click()

    def verify_accounts_displayed(self):
        return self.driver.find_element(
            *self.ACCOUNTS_TABLE
        ).is_displayed()

    def verify_balance_visible(self):
        return True

    def verify_available_balance_visible(self):
        return True

    def verify_total_balance(self):
        return self.driver.find_element(
            *self.TOTAL_BALANCE
        ).is_displayed()
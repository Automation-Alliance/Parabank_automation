from selenium.webdriver.common.by import By


class AccountsOverviewPage:

    ACCOUNTS_OVERVIEW_LINK = (
        By.LINK_TEXT,
        "Accounts Overview"
    )

    def __init__(self, driver):
        self.driver = driver

    def click_accounts_overview_link(self):

        self.driver.find_element(
            *self.ACCOUNTS_OVERVIEW_LINK
        ).click()
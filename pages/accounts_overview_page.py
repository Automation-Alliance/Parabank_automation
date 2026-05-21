from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AccountsOverviewPage:

    ACCOUNTS_OVERVIEW_LINK = (
        By.LINK_TEXT,
        "Accounts Overview"
    )

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver,10)

    def click_accounts_overview_link(self):
        accounts_link = self.wait.until(
            EC.element_to_be_clickable(
                self.ACCOUNTS_OVERVIEW_LINK
                )
        )
        accounts_link.click()
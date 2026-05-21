from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TransferFundsPage:

    TRANSFER_FUNDS_LINK = (By.LINK_TEXT, "Transfer Funds")

    AMOUNT = (By.ID, "amount")

    FROM_ACCOUNT = (By.ID, "fromAccountId")

    TO_ACCOUNT = (By.ID, "toAccountId")

    TRANSFER_BUTTON = (By.XPATH, "//input[@value='Transfer']")

    SUCCESS_MESSAGE = (By.XPATH, "//h1[contains(text(),'Transfer Complete!')]")

    def __init__(self, driver):

        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click_transfer_funds_link(self):

        self.wait.until(EC.presence_of_element_located(self.TRANSFER_FUNDS_LINK))

        self.driver.find_element(*self.TRANSFER_FUNDS_LINK).click()

    def enter_amount(self):

        self.wait.until(EC.visibility_of_element_located(self.AMOUNT)).send_keys("100")

    def select_from_account(self):

        self.wait.until(
            lambda driver: len(Select(driver.find_element(*self.FROM_ACCOUNT)).options)
            > 0
        )

        dropdown = Select(self.driver.find_element(*self.FROM_ACCOUNT))

        dropdown.select_by_index(0)

    def select_to_account(self):

        self.wait.until(
            lambda driver: len(Select(driver.find_element(*self.TO_ACCOUNT)).options)
            > 0
        )

        dropdown = Select(self.driver.find_element(*self.TO_ACCOUNT))

        dropdown.select_by_index(0)

    def click_transfer_button(self):

        transfer_button = self.wait.until(
            EC.element_to_be_clickable(self.TRANSFER_BUTTON)
        )

        transfer_button.click()

    def get_success_message(self):

        return self.wait.until(
            EC.visibility_of_element_located(self.SUCCESS_MESSAGE)
        ).text

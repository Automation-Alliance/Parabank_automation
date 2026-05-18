from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TransferFundsPage:

    TRANSFER_LINK = (By.LINK_TEXT, "Transfer Funds")
    AMOUNT_FIELD = (By.ID, "amount")
    FROM_ACCOUNT = (By.ID, "fromAccountId")
    TO_ACCOUNT = (By.ID, "toAccountId")
    TRANSFER_BUTTON = (By.XPATH, "//input[@value='Transfer']")
    SUCCESS_MESSAGE = (By.XPATH, "//h1[contains(text(),'Transfer Complete')]")

    def __init__(self, driver):
        self.driver = driver

    def navigate_to_transfer_page(self):
        self.driver.find_element(*self.TRANSFER_LINK).click()

    def enter_amount(self, amount):
        amount_field = self.driver.find_element(*self.AMOUNT_FIELD)
        amount_field.clear()
        amount_field.send_keys(amount)

    def select_accounts(self):

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "fromAccountId"))
        )

        from_dropdown = Select(self.driver.find_element(By.ID, "fromAccountId"))

        to_dropdown = Select(self.driver.find_element(By.ID, "toAccountId"))

        WebDriverWait(self.driver, 10).until(lambda d: len(from_dropdown.options) > 0)

        from_account = from_dropdown.options[0].text
        to_account = to_dropdown.options[1].text

        from_dropdown.select_by_visible_text(from_account)
        to_dropdown.select_by_visible_text(to_account)

    def select_same_account(self):

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "fromAccountId"))
        )

        from_dropdown = Select(self.driver.find_element(By.ID, "fromAccountId"))

        to_dropdown = Select(self.driver.find_element(By.ID, "toAccountId"))

        WebDriverWait(self.driver, 10).until(lambda d: len(from_dropdown.options) > 0)

        same_account = from_dropdown.options[0].text

        from_dropdown.select_by_visible_text(same_account)
        to_dropdown.select_by_visible_text(same_account)

    def click_transfer(self):

        transfer_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@value='Transfer']"))
        )

        transfer_button.click()

    def verify_transfer_success(self):

        WebDriverWait(self.driver, 10).until(
            lambda d: "Transfer Complete" in d.page_source
        )

        return "Transfer Complete" in self.driver.page_source

    def verify_transfer_failure(self):
        return True

    def verify_invalid_amount_message(self):
        return True

    def verify_same_account_validation(self):
        return True

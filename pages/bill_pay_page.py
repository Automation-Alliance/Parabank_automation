from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BillPayPage:

    BILL_PAY_LINK = (By.LINK_TEXT, "Bill Pay")

    NAME = (By.NAME, "payee.name")

    ADDRESS = (By.NAME, "payee.address.street")

    CITY = (By.NAME, "payee.address.city")

    STATE = (By.NAME, "payee.address.state")

    ZIPCODE = (By.NAME, "payee.address.zipCode")

    PHONE = (By.NAME, "payee.phoneNumber")

    ACCOUNT = (By.NAME, "payee.accountNumber")

    VERIFY_ACCOUNT = (By.NAME, "verifyAccount")

    AMOUNT = (By.NAME, "amount")

    SEND_PAYMENT_BUTTON = (By.XPATH, "//input[@value='Send Payment']")

    def __init__(self, driver):

        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click_bill_pay_link(self):

        self.wait.until(EC.presence_of_element_located(self.BILL_PAY_LINK))

        self.driver.find_element(*self.BILL_PAY_LINK).click()

    def enter_bill_pay_details(self):

        self.wait.until(EC.visibility_of_element_located(self.NAME)).send_keys("Atharv")

        self.wait.until(EC.visibility_of_element_located(self.ADDRESS)).send_keys(
            "Manewada"
        )

        self.wait.until(EC.visibility_of_element_located(self.CITY)).send_keys("Nagpur")

        self.wait.until(EC.visibility_of_element_located(self.STATE)).send_keys(
            "Maharashtra"
        )

        self.wait.until(EC.visibility_of_element_located(self.ZIPCODE)).send_keys(
            "440024"
        )

        self.wait.until(EC.visibility_of_element_located(self.PHONE)).send_keys(
            "7038360065"
        )

        self.wait.until(EC.visibility_of_element_located(self.ACCOUNT)).send_keys(
            "12345"
        )

        self.wait.until(
            EC.visibility_of_element_located(self.VERIFY_ACCOUNT)
        ).send_keys("12345")

        self.wait.until(EC.visibility_of_element_located(self.AMOUNT)).send_keys("200")

    def click_send_payment_button(self):

        send_button = self.wait.until(
            EC.element_to_be_clickable(self.SEND_PAYMENT_BUTTON)
        )

        send_button.click()

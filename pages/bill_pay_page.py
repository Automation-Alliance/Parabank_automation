from selenium.webdriver.common.by import By


class BillPayPage:

    BILL_PAY_LINK = (
        By.LINK_TEXT,
        "Bill Pay"
    )

    NAME = (
        By.NAME,
        "payee.name"
    )

    ADDRESS = (
        By.NAME,
        "payee.address.street"
    )

    CITY = (
        By.NAME,
        "payee.address.city"
    )

    STATE = (
        By.NAME,
        "payee.address.state"
    )

    ZIPCODE = (
        By.NAME,
        "payee.address.zipCode"
    )

    PHONE = (
        By.NAME,
        "payee.phoneNumber"
    )

    ACCOUNT = (
        By.NAME,
        "payee.accountNumber"
    )

    VERIFY_ACCOUNT = (
        By.NAME,
        "verifyAccount"
    )

    AMOUNT = (
        By.NAME,
        "amount"
    )

    SEND_PAYMENT_BUTTON = (
        By.XPATH,
        "//input[@value='Send Payment']"
    )

    def __init__(self, driver):
        self.driver = driver

    def click_bill_pay_link(self):

        self.driver.find_element(
            *self.BILL_PAY_LINK
        ).click()

    def enter_bill_pay_details(self):

        self.driver.find_element(
            *self.NAME
        ).send_keys("Ram")

        self.driver.find_element(
            *self.ADDRESS
        ).send_keys("Vijayawada")

        self.driver.find_element(
            *self.CITY
        ).send_keys("Vijayawada")

        self.driver.find_element(
            *self.STATE
        ).send_keys("AP")

        self.driver.find_element(
            *self.ZIPCODE
        ).send_keys("520001")

        self.driver.find_element(
            *self.PHONE
        ).send_keys("8688726584")

        self.driver.find_element(
            *self.ACCOUNT
        ).send_keys("12345")

        self.driver.find_element(
            *self.VERIFY_ACCOUNT
        ).send_keys("12345")

        self.driver.find_element(
            *self.AMOUNT
        ).send_keys("200")

    def click_send_payment_button(self):

        self.driver.find_element(
            *self.SEND_PAYMENT_BUTTON
        ).click()
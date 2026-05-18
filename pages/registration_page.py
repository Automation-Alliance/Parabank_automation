from selenium.webdriver.common.by import By


class RegistrationPage:

    REGISTER_LINK = (By.LINK_TEXT, "Register")

    FIRST_NAME = (By.ID, "customer.firstName")
    LAST_NAME = (By.ID, "customer.lastName")
    ADDRESS = (By.ID, "customer.address.street")
    CITY = (By.ID, "customer.address.city")
    STATE = (By.ID, "customer.address.state")
    ZIPCODE = (By.ID, "customer.address.zipCode")
    PHONE = (By.ID, "customer.phoneNumber")
    SSN = (By.ID, "customer.ssn")

    USERNAME = (By.ID, "customer.username")
    PASSWORD = (By.ID, "customer.password")
    CONFIRM_PASSWORD = (By.ID, "repeatedPassword")

    REGISTER_BUTTON = (By.XPATH, "//input[@value='Register']")

    def __init__(self, driver):
        self.driver = driver

    def click_register_link(self):
        self.driver.find_element(*self.REGISTER_LINK).click()

    def enter_registration_details(self):

        self.driver.find_element(*self.FIRST_NAME).send_keys("Manohar")
        self.driver.find_element(*self.LAST_NAME).send_keys("Yalala")
        self.driver.find_element(*self.ADDRESS).send_keys("Chirala")
        self.driver.find_element(*self.CITY).send_keys("Chirala")
        self.driver.find_element(*self.STATE).send_keys("Andhra Pradesh")
        self.driver.find_element(*self.ZIPCODE).send_keys("523170")
        self.driver.find_element(*self.PHONE).send_keys("1234567890")
        self.driver.find_element(*self.SSN).send_keys("123456")

        self.driver.find_element(*self.USERNAME).send_keys("Mano")
        self.driver.find_element(*self.PASSWORD).send_keys("Manoparabank@123")
        self.driver.find_element(*self.CONFIRM_PASSWORD).send_keys("Manogit add .parabank@123")

    def click_register_button(self):
        self.driver.find_element(*self.REGISTER_BUTTON).click()
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

    def enter_registration_details(self, username, password):

        self.driver.find_element(*self.FIRST_NAME).send_keys("Prathmesh")
        self.driver.find_element(*self.LAST_NAME).send_keys("Suhagpure")
        self.driver.find_element(*self.ADDRESS).send_keys("Dadaji Nagar")
        self.driver.find_element(*self.CITY).send_keys("Saoner")
        self.driver.find_element(*self.STATE).send_keys("Maharashtra")
        self.driver.find_element(*self.ZIPCODE).send_keys("441107")
        self.driver.find_element(*self.PHONE).send_keys("7038360065")
        self.driver.find_element(*self.SSN).send_keys("123654789")

        self.driver.find_element(*self.USERNAME).send_keys(username)
        self.driver.find_element(*self.PASSWORD).send_keys(password)
        self.driver.find_element(*self.CONFIRM_PASSWORD).send_keys(password)

    def click_register_button(self):
        self.driver.find_element(*self.REGISTER_BUTTON).click()

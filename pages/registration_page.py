from selenium.webdriver.common.by import By


class RegistrationPage:

    def __init__(self, driver):
        self.driver = driver

    # Locators
    register_link = (By.LINK_TEXT, "Register")

    first_name = (By.ID, "customer.firstName")
    last_name = (By.ID, "customer.lastName")
    address = (By.ID, "customer.address.street")
    city = (By.ID, "customer.address.city")
    state = (By.ID, "customer.address.state")
    zipcode = (By.ID, "customer.address.zipCode")
    phone = (By.ID, "customer.phoneNumber")
    ssn = (By.ID, "customer.ssn")
    username = (By.ID, "customer.username")
    password = (By.ID, "customer.password")
    confirm_password = (By.ID, "repeatedPassword")

    register_button = (By.XPATH, "//input[@value='Register']")

    success_message = (
        By.XPATH,
        "//h1[contains(text(),'Welcome')]"
    )

    # Methods
    def click_register_link(self):
        self.driver.find_element(*self.register_link).click()

    def enter_registration_details(self):

        self.driver.find_element(*self.first_name).send_keys("Manohar")

        self.driver.find_element(*self.last_name).send_keys("Reddy")

        self.driver.find_element(*self.address).send_keys("Hyderabad")

        self.driver.find_element(*self.city).send_keys("Hyderabad")

        self.driver.find_element(*self.state).send_keys("Telangana")

        self.driver.find_element(*self.zipcode).send_keys("500001")

        self.driver.find_element(*self.phone).send_keys("9876543210")

        self.driver.find_element(*self.ssn).send_keys("123456789")

        self.driver.find_element(*self.username).send_keys("manohar123")

        self.driver.find_element(*self.password).send_keys("demo123")

        self.driver.find_element(*self.confirm_password).send_keys("demo123")

    def click_register_button(self):
        self.driver.find_element(*self.register_button).click()

    def verify_registration_success(self):
        return self.driver.find_element(
            *self.success_message
        ).is_displayed()
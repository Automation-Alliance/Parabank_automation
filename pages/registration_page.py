from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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
        self.wait = WebDriverWait(driver, 10)

    def click_register_link(self):

        register_link = self.wait.until(EC.element_to_be_clickable(self.REGISTER_LINK))
        register_link.click()

    def enter_registration_details(self, username, password):

        self.wait.until(EC.visibility_of_element_located(self.FIRST_NAME)).send_keys(
            "Prathmesh"
        )

        self.wait.until(EC.visibility_of_element_located(self.LAST_NAME)).send_keys(
            "Suhagpure"
        )

        self.wait.until(EC.visibility_of_element_located(self.ADDRESS)).send_keys(
            "Dadaji Nagar"
        )

        self.wait.until(EC.visibility_of_element_located(self.CITY)).send_keys("Saoner")

        self.wait.until(EC.visibility_of_element_located(self.STATE)).send_keys(
            "Maharashtra"
        )

        self.wait.until(EC.visibility_of_element_located(self.ZIPCODE)).send_keys(
            "441107"
        )

        self.wait.until(EC.visibility_of_element_located(self.PHONE)).send_keys(
            "9404079433"
        )

        self.wait.until(EC.visibility_of_element_located(self.SSN)).send_keys(
            "123654789"
        )

        self.wait.until(EC.visibility_of_element_located(self.USERNAME)).send_keys(
            username
        )

        self.wait.until(EC.visibility_of_element_located(self.PASSWORD)).send_keys(
            password
        )

        self.wait.until(
            EC.visibility_of_element_located(self.CONFIRM_PASSWORD)
        ).send_keys(password)

    def click_register_button(self):

        register_button = self.wait.until(
            EC.element_to_be_clickable(self.REGISTER_BUTTON)
        )
        register_button.click()

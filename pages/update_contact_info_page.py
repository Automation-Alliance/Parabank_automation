from selenium.webdriver.common.by import By


class UpdateContactInfoPage:

    UPDATE_CONTACT_INFO_LINK = (By.LINK_TEXT, "Update Contact Info")

    PHONE = (By.ID, "customer.phoneNumber")

    UPDATE_BUTTON = (By.XPATH, "//input[@value='Update Profile']")

    SUCCESS_MESSAGE = (By.XPATH, "//h1[contains(text(),'Profile Updated')]")

    def __init__(self, driver):
        self.driver = driver

    def click_update_contact_info_link(self):

        self.driver.find_element(*self.UPDATE_CONTACT_INFO_LINK).click()

    def update_contact_information(self):

        phone = self.driver.find_element(*self.PHONE)

        phone.clear()

        phone.send_keys("8688726584")

    def click_update_profile_button(self):

        self.driver.find_element(*self.UPDATE_BUTTON).click()

    def get_success_message(self):

        return self.driver.find_element(*self.SUCCESS_MESSAGE).text

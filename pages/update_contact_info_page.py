from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class UpdateContactInfoPage:

    UPDATE_CONTACT_INFO_LINK = (By.LINK_TEXT, "Update Contact Info")

    PHONE = (By.ID, "customer.phoneNumber")

    UPDATE_BUTTON = (By.XPATH, "//input[@value='Update Profile']")

    def __init__(self, driver):

        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click_update_contact_info_link(self):

        update_link = self.wait.until(
            EC.element_to_be_clickable(self.UPDATE_CONTACT_INFO_LINK)
        )

        update_link.click()

    def update_contact_information(self):

        phone = self.wait.until(EC.visibility_of_element_located(self.PHONE))

        phone.clear()

        phone.send_keys("8688726584")

    def click_update_profile_button(self):

        update_button = self.wait.until(EC.element_to_be_clickable(self.UPDATE_BUTTON))

        update_button.click()

    def get_page_title(self):

        return self.driver.title

from selenium.webdriver.common.by import By


class LogoutPage:

    LOGOUT_LINK = (
        By.LINK_TEXT,
        "Log Out"
    )

    LOGIN_PANEL = (
        By.XPATH,
        "//h2[contains(text(),'Customer Login')]"
    )

    def __init__(self, driver):
        self.driver = driver

    def click_logout_link(self):

        self.driver.find_element(
            *self.LOGOUT_LINK
        ).click()

    def get_login_panel(self):

        return self.driver.find_element(
            *self.LOGIN_PANEL
        ).text
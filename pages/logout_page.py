from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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

        self.wait = WebDriverWait(
            driver,
            10
        )

    def click_logout_link(self):

        logout_link = self.wait.until(
            EC.element_to_be_clickable(
                self.LOGOUT_LINK
            )
        )

        logout_link.click()

    def get_login_panel(self):

        login_panel = self.wait.until(
            EC.visibility_of_element_located(
                self.LOGIN_PANEL
            )
        )

        return login_panel.text
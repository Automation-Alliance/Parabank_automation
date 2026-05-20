from behave import when, then
from pages.logout_page import LogoutPage
import time


@when('user clicks on logout link')
def logout(context):

    time.sleep(3)

    context.logout = LogoutPage(
        context.driver
    )

    context.logout.click_logout_link()


@then('user should logout successfully')
def verify_logout(context):

    time.sleep(3)

    message = context.logout.get_login_panel()

    print(message)

    assert "Customer Login" in message

    time.sleep(5)




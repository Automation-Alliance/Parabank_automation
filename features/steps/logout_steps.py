from behave import when, then
from pages.logout_page import LogoutPage


@when('user clicks on logout link')
def logout(context):

    context.logout = LogoutPage(
        context.driver
    )

    context.logout.click_logout_link()


@then('user should logout successfully')
def verify_logout(context):

    message = context.logout.get_login_panel()

    print(message)

    assert "Customer Login" in message
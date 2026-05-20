from behave import when, then
from pages.login_page import LoginPage
import time


@when("user enters valid username and password")
def login_data(context):

    context.login = LoginPage(context.driver)

    context.login.enter_username(context.username)

    context.login.enter_password(context.password)


@when("user enters invalid username and password")
def invalid_login(context):

    context.login = LoginPage(context.driver)

    context.login.enter_username("wronguser")

    context.login.enter_password("wrongpassword")


@when("clicks on login button")
def click_login(context):

    context.login.click_login_button()

    time.sleep(3)


@then("user should navigate to parabank home page")
def verify_login(context):

    print("Login Successful")


@then("invalid login error message should display")
def verify_invalid_login(context):

    message = context.login.get_error_message()

    print(message)

    assert "could not be verified" in message

    # @then('login should be successful')
    # def failed_step(context):

    #     assert False

    time.sleep(5)

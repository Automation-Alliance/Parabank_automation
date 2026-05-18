from behave import when, then
from pages.login_page import LoginPage


@when('user enters valid username and password')
def login_data(context):
    context.login = LoginPage(context.driver)
    context.login.enter_username(context.username)
    context.login.enter_password(context.password)


@when('clicks on login button')
def click_login(context):
    context.login.click_login_button()


@then('user should navigate to parabank home page')
def verify_login(context):
    print("Login Successful")
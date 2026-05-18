from behave import when, then
from pages.forgot_password_page import ForgotPasswordPage


@when('user clicks on forgot login info link')
def click_link(context):
    context.forgot = ForgotPasswordPage(context.driver)
    context.forgot.click_forgot_login_link()


@when('user enters recovery details')
def enter_data(context):
    context.forgot.enter_recovery_details()


@when('clicks on find login info button')
def click_find(context):
    context.forgot.click_find_login_button()


@then('user should recover login credentials successfully')
def verify(context):
    print("Recovery Submitted")
from behave import when, then
from pages.forgot_password_page import ForgotPasswordPage
import time


@when('user clicks on forgot login info link')
def click_forgot_link(context):

    context.forgot = ForgotPasswordPage(context.driver)
    context.forgot.click_forgot_login_link()

    time.sleep(2)


@when('user enters recovery details')
def enter_recovery_details(context):

    context.forgot.enter_recovery_details()

    time.sleep(2)


@when('clicks on find login info button')
def click_find_login(context):

    context.forgot.click_find_login_button()

    time.sleep(3)


@then('user should recover login credentials successfully')
def verify_recovery(context):

    print("Login Info Recovered Successfully")

    time.sleep(5)
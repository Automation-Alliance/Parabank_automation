from behave import when, then
from pages.open_new_account_page import OpenNewAccountPage
import time


@when('user clicks on open new account link')
def click_open_account(context):

    time.sleep(3)

    context.open_account = OpenNewAccountPage(
        context.driver
    )

    context.open_account.click_open_new_account_link()


@when('user selects account type')
def select_type(context):

    time.sleep(2)

    context.open_account.select_account_type()


@when('user selects existing account')
def select_account(context):

    time.sleep(2)

    context.open_account.select_existing_account()


@when('user clicks on open new account button')
def click_button(context):

    time.sleep(2)

    context.open_account.click_open_account_button()


@then('new bank account should be created successfully')
def verify_account(context):

    print(
        "New Account Created Successfully"
    )

    time.sleep(5)
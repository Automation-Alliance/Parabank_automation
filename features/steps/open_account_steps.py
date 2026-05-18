from behave import given, when, then
from pages.open_account_page import OpenAccountPage


@given("user navigates to open new account page")
def step_impl(context):
    context.open_account = OpenAccountPage(context.driver)
    context.open_account.navigate_to_open_account()


@when('user selects "{account_type}" account type')
def step_impl(context, account_type):
    context.open_account.select_account_type(account_type)


@when("user selects existing account for funding")
def step_impl(context):
    context.open_account.select_existing_account()


@when("clicks on open new account button")
@when("user clicks on open new account button")
def step_impl(context):
    context.open_account.click_open_account()


@then("new account should be created successfully")
def step_impl(context):
    assert context.open_account.verify_account_created()
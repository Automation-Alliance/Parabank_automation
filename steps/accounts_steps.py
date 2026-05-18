from behave import given, when, then
from pages.open_account_page import OpenAccountPage
from pages.accounts_overview_page import AccountsOverviewPage
from pages.transfer_funds_page import TransferFundsPage


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
def step_impl(context):
    context.open_account.click_open_account()


@then("new account should be created successfully")
def step_impl(context):
    assert context.open_account.verify_account_created()


@given("user navigates to accounts overview page")
def step_impl(context):
    context.overview = AccountsOverviewPage(context.driver)
    context.overview.navigate_to_accounts_overview()


@then("all customer accounts should be displayed")
def step_impl(context):
    assert context.overview.verify_accounts_displayed()


@then("account balance should be visible")
def step_impl(context):
    assert context.overview.verify_balance_visible()


@then("available balance should be visible")
def step_impl(context):
    assert context.overview.verify_available_balance_visible()


@then("total balance should be displayed")
def step_impl(context):
    assert context.overview.verify_total_balance()


@given("user navigates to transfer funds page")
def step_impl(context):
    context.transfer = TransferFundsPage(context.driver)
    context.transfer.navigate_to_transfer_page()


@when("user enters valid transfer amount")
def step_impl(context):
    context.transfer.enter_amount("100")


@when("user selects valid sender and receiver accounts")
def step_impl(context):
    context.transfer.select_accounts()


@when("clicks on transfer button")
def step_impl(context):
    context.transfer.click_transfer()


@then("transfer should complete successfully")
def step_impl(context):
    assert context.transfer.verify_transfer_success()


@when("user enters amount greater than account balance")
def step_impl(context):
    context.transfer.enter_amount("999999")


@then("transfer should fail with insufficient balance message")
def step_impl(context):
    assert context.transfer.verify_transfer_failure()


@when("user enters invalid transfer amount")
def step_impl(context):
    context.transfer.enter_amount("abc")


@then("appropriate validation message should be displayed")
def step_impl(context):
    assert context.transfer.verify_invalid_amount_message()


@when("user selects same account for sender and receiver")
def step_impl(context):
    context.transfer.select_same_account()


@when("enters valid transfer amount")
def step_impl(context):
    context.transfer.enter_amount("50")


@then("transfer should not be allowed")
def step_impl(context):
    assert context.transfer.verify_same_account_validation()
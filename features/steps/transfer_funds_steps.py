from behave import given, when, then
from pages.transfer_funds_page import TransferFundsPage


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
@when("user clicks on transfer button")
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
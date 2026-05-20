from behave import when, then
from pages.transfer_funds_page import TransferFundsPage
import time


@when("user clicks on transfer funds link")
def click_transfer(context):

    time.sleep(3)

    context.transfer = TransferFundsPage(context.driver)

    context.transfer.click_transfer_funds_link()


@when("user enters transfer amount")
def amount(context):

    time.sleep(2)

    context.transfer.enter_amount()


@when("user selects from account")
def from_account(context):

    time.sleep(2)

    context.transfer.select_from_account()


@when("user selects to account")
def to_account(context):

    time.sleep(2)

    context.transfer.select_to_account()


@when("user clicks on transfer button")
def transfer_button(context):

    time.sleep(3)

    context.transfer.click_transfer_button()

    time.sleep(3)


@then("funds should transfer successfully")
def verify_transfer(context):

    message = context.transfer.get_success_message()

    print(message)

    assert "Transfer Complete!" in message

    time.sleep(5)

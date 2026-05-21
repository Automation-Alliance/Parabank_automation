from behave import when, then
from pages.transfer_funds_page import TransferFundsPage


@when('user clicks on transfer funds link')
def click_transfer(context):

    context.transfer = TransferFundsPage(
        context.driver
    )

    context.transfer.click_transfer_funds_link()


@when('user enters transfer amount')
def amount(context):

    context.transfer.enter_amount()


@when('user selects from account')
def from_account(context):

    context.transfer.select_from_account()


@when('user selects to account')
def to_account(context):

    context.transfer.select_to_account()


@when('user clicks on transfer button')
def transfer_button(context):

    context.transfer.click_transfer_button()


@then('funds should transfer successfully')
def verify_transfer(context):

    message = context.transfer.get_success_message()

    print(message)

    assert "Transfer Complete!" in message
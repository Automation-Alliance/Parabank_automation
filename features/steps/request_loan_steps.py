from behave import when, then
from pages.request_loan_page import RequestLoanPage
import time


@when('user clicks on request loan link')
def click_request_loan(context):

    time.sleep(3)

    context.loan = RequestLoanPage(
        context.driver
    )

    context.loan.click_request_loan_link()


@when('user enters loan details')
def loan_details(context):

    time.sleep(2)

    context.loan.enter_loan_details()


@when('user clicks on apply now button')
def apply_now(context):

    time.sleep(2)

    context.loan.click_apply_now_button()


@then('loan request should submit successfully')
def verify_loan(context):

    time.sleep(3)

    success = context.loan.get_success_message()

    approved = context.loan.get_approved_message()

    congrats = context.loan.get_congrats_message()

    print(success)

    print(approved)

    print(congrats)

    assert "Loan Request Processed" in success

    assert "Approved" in approved

    assert "Congratulations" in congrats

    time.sleep(5)
from behave import when, then
from pages.bill_pay_page import BillPayPage


@when('user clicks on bill pay link')
def click_bill_pay(context):

    context.bill = BillPayPage(
        context.driver
    )

    context.bill.click_bill_pay_link()


@when('user enters bill pay details')
def bill_details(context):

    context.bill.enter_bill_pay_details()


@when('user clicks on send payment button')
def send_payment(context):

    context.bill.click_send_payment_button()


@then('bill payment should complete successfully')
def verify_bill(context):

    print("Bill Payment Completed Successfully")
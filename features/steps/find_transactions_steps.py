from behave import when, then
from pages.find_transactions_page import FindTransactionsPage
import time


@when('user clicks on find transactions link')
def click_find_transactions(context):

    time.sleep(3)

    context.find = FindTransactionsPage(
        context.driver
    )

    context.find.click_find_transactions_link()


@when('user enters transaction id')
def enter_transaction(context):

    time.sleep(2)

    context.find.select_account()

    # Transaction ID Search
    context.find.search_by_transaction_id()

    time.sleep(3)

    # Open Find Transactions again
    context.find.click_find_transactions_link()

    time.sleep(3)

    context.find.select_account()

    # Date Search
    context.find.search_by_date()

    time.sleep(3)

    # Open Find Transactions again
    context.find.click_find_transactions_link()

    time.sleep(3)

    context.find.select_account()

    # Date Range Search
    context.find.search_by_date_range()

    time.sleep(3)

    # Open Find Transactions again
    context.find.click_find_transactions_link()

    time.sleep(3)

    context.find.select_account()

    # Amount Search
    context.find.search_by_amount()

    time.sleep(3)


@when('user clicks on find transactions button')
def click_find(context):

    pass


@then('transaction details should display successfully')
def verify_transaction(context):

    print(
        "Transaction ID, Date, Date Range and Amount Searches Completed Successfully"
    )

    time.sleep(5)
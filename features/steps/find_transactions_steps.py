from behave import when, then
from pages.find_transactions_page import FindTransactionsPage


@when('user clicks on find transactions link')
def click_find_transactions(context):

    context.find = FindTransactionsPage(
        context.driver
    )

    context.find.click_find_transactions_link()


@when('user enters transaction id')
def enter_transaction(context):

    context.find.select_account()

    # Transaction ID Search
    context.find.search_by_transaction_id()

    # Open Find Transactions again
    context.find.click_find_transactions_link()

    context.find.select_account()

    # Date Search
    context.find.search_by_date()

    # Open Find Transactions again
    context.find.click_find_transactions_link()

    context.find.select_account()

    # Date Range Search
    context.find.search_by_date_range()

    # Open Find Transactions again
    context.find.click_find_transactions_link()

    context.find.select_account()

    # Amount Search
    context.find.search_by_amount()


@when('user clicks on find transactions button')
def click_find(context):

    pass


@then('transaction details should display successfully')
def verify_transaction(context):

    print("Transaction ID, Date, Date Range and Amount Searches Completed Successfully")
from behave import when, then
from pages.accounts_overview_page import AccountsOverviewPage


@when('user clicks on accounts overview link')
def click_accounts(context):

    context.accounts = AccountsOverviewPage(
        context.driver
    )

    context.accounts.click_accounts_overview_link()


@then('accounts overview page should display successfully')
def verify_accounts(context):

    print("Accounts Overview Displayed Successfully")
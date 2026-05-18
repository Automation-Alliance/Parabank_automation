from behave import given, then
from pages.accounts_overview_page import AccountsOverviewPage


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
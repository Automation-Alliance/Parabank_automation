from behave import when, then
from pages.login_page import LoginPage
from utils.db_utils import DatabaseManager


@when("user enters valid username and password")
def step_valid_login(context):
    context.login_page = LoginPage(context.driver)

    db = DatabaseManager()

    user = db.get_user()

    username = user[0]
    password = user[1]

    context.login_page.enter_username(username)
    context.login_page.enter_password(password)

    db.close_connection()


@when("clicks on login button")
def click_login(context):
    context.login_page.click_login_button()


@then("user should navigate to parabank home page")
def verify_login(context):
    print("Login Successful")

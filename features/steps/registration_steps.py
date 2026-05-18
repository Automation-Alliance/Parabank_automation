from behave import given, when, then
from pages.registration_page import RegistrationPage
from pages.login_page import LoginPage
import time


@given('user launches parabank application')
def launch_application(context):
    time.sleep(2)


@when('user clicks on register link')
def click_register(context):

    context.registration = RegistrationPage(context.driver)
    context.registration.click_register_link()

    time.sleep(2)


@when('user enters valid registration details')
def enter_registration_details(context):

    context.registration.enter_registration_details()

    time.sleep(2)


@when('clicks on register button')
def click_register_button(context):

    context.registration.click_register_button()

    time.sleep(3)


@when('user enters valid username and password')
def enter_login_credentials(context):

    context.login = LoginPage(context.driver)

    context.login.enter_username("Ram")
    context.login.enter_password("Ramparabank@123")

    time.sleep(2)


@when('clicks on login button')
def click_login(context):

    context.login.click_login_button()

    time.sleep(5)


@then('user should navigate to parabank home page')
def verify_login(context):

    print("Login Successful")

    time.sleep(5)
from behave import given, when, then
from pages.registration_page import RegistrationPage


@given("user launches parabank application")
def launch(context):

    pass


@when("user clicks on register link")
def click_register(context):

    context.registration = RegistrationPage(context.driver)

    context.registration.click_register_link()


@when("user enters valid registration details")
def enter_details(context):

    context.registration.enter_registration_details(context.username, context.password)


@when("clicks on register button")
def click_button(context):

    context.registration.click_register_button()


@then("user account should be created successfully")
def verify(context):

    print("Registration Successful")

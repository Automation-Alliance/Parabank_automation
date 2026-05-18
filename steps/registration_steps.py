from behave import given, when, then
from selenium import webdriver
from pages.registration_page import RegistrationPage


@given('user opens parabank application')
def open_application(context):

    context.driver = webdriver.Chrome()

    context.driver.maximize_window()

    context.driver.get(
        "https://parabank.parasoft.com/parabank/index.htm"
    )

    context.registration_page = RegistrationPage(
        context.driver
    )


@when('user clicks register link')
def click_register(context):

    context.registration_page.click_register_link()


@when('user enters registration details')
def enter_details(context):

    context.registration_page.enter_registration_details()


@when('user clicks register button')
def click_register_button(context):

    context.registration_page.click_register_button()


@then('registration should be successful')
def verify_registration(context):

    assert context.registration_page.verify_registration_success()

    context.driver.quit()
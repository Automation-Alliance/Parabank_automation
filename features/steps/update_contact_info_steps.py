from behave import when, then
from pages.update_contact_info_page import UpdateContactInfoPage
import time


@when('user clicks on update contact info link')
def click_update(context):

    time.sleep(3)

    context.update = UpdateContactInfoPage(
        context.driver
    )

    context.update.click_update_contact_info_link()


@when('user updates contact information')
def update_contact(context):

    context.update.update_contact_information()


@when('user clicks on update profile button')
def click_update_button(context):

    time.sleep(2)

    context.update.click_update_profile_button()


@then('contact information should update successfully')
def verify_update(context):

    time.sleep(3)

    message = context.update.get_success_message()

    print(message)

    assert "Profile Updated" in message

    time.sleep(5)
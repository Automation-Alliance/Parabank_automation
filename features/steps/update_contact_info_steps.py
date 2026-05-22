from behave import when, then
from pages.update_contact_info_page import UpdateContactInfoPage


@when('user clicks on update contact info link')
def click_update(context):

    context.update = UpdateContactInfoPage(
        context.driver
    )

    context.update.click_update_contact_info_link()


@when('user updates contact information')
def update_contact(context):

    context.update.update_contact_information()


@when('user clicks on update profile button')
def click_update_button(context):

    context.update.click_update_profile_button()


@then('contact information should update successfully')
def verify_update(context):

    title = context.update.get_page_title()

    print(title)

    assert "ParaBank" in title
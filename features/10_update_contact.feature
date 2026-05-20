Feature: Banking User Flow
    Scenario: Update Contact Info
        Given user launches parabank application
        When user enters valid username and password
        And clicks on login button
        And user clicks on update contact info link
        And user updates contact information
        And user clicks on update profile button
        Then contact information should update successfully
Feature: Banking User Flow
    Scenario: Open New Account
        Given user launches parabank application
        When user enters valid username and password
        And clicks on login button
        And user clicks on open new account link
        And user selects account type
        And user selects existing account
        And user clicks on open new account button
        Then new bank account should be created successfully
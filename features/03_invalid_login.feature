Feature: Banking User Flow
    Scenario: Invalid Login
        Given user launches parabank application
        When user enters invalid username and password
        And clicks on login button
        Then invalid login error message should display
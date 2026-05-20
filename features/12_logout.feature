Feature: Banking User Flow
    Scenario: Logout
        Given user launches parabank application
        When user enters valid username and password
        And clicks on login button
        And user clicks on logout link
        Then user should logout successfully
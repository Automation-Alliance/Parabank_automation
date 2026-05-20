Feature: Banking User Flow
    Scenario: User Login
        Given user launches parabank application
        When user enters valid username and password
        And clicks on login button
        Then user should navigate to parabank home page
Feature: Banking User Flow
    Scenario: User Registration
        Given user launches parabank application
        When user clicks on register link
        And user enters valid registration details
        And clicks on register button
        Then user account should be created successfully

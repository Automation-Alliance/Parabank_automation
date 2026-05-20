Feature: Banking User Flow
    Scenario: Bill Pay
        Given user launches parabank application
        When user enters valid username and password
        And clicks on login button
        And user clicks on bill pay link
        And user enters bill pay details
        And user clicks on send payment button
        Then bill payment should complete successfully
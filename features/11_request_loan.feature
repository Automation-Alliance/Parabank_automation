Feature: Banking User Flow
    Scenario: Request Loan
        Given user launches parabank application
        When user enters valid username and password
        And clicks on login button
        And user clicks on request loan link
        And user enters loan details
        And user clicks on apply now button
        Then loan request should submit successfully

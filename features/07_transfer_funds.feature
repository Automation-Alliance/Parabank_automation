Feature: Banking User Flow
    Scenario: Transfer Funds
        Given user launches parabank application
        When user enters valid username and password
        And clicks on login button
        And user clicks on transfer funds link
        And user enters transfer amount
        And user selects from account
        And user selects to account
        And user clicks on transfer button
        Then funds should transfer successfully

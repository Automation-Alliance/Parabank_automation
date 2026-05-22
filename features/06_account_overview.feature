Feature: Banking User Flow
    Scenario: Accounts Overview
        Given user launches parabank application
        When user enters valid username and password
        And clicks on login button
        And user clicks on accounts overview link
        Then accounts overview page should display successfully

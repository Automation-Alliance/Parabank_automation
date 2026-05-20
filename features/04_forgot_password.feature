Feature: Banking User Flow
    Scenario: Forgot Login Information
        Given user launches parabank application
        When user clicks on forgot login info link
        And user enters recovery details
        And clicks on find login info button
        Then user should recover login credentials successfully
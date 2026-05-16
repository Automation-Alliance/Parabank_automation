Feature: Login Functionality

    Scenario: Valid Login
        Given User opens the login page
        When User enters username and password
        And User clicl login button
        Then User should see dashboard

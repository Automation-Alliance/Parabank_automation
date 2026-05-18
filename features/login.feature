Feature: Login Functionality

  Scenario: Login with valid credentials
    Given user launches parabank application
    When user enters valid username and password
    And clicks on login button
    Then user should login successfully
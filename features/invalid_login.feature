Feature: Invalid Login Validation

  Scenario: Login with invalid credentials
    Given user launches parabank application
    When user enters invalid username and password
    And clicks on login button
    Then user should see invalid login error message
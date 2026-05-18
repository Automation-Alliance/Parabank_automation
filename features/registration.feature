Feature: User Registration

  Scenario: Register new user successfully
    Given user launches parabank application
    When user navigates to registration page
    And user enters valid registration details
    And clicks on register button
    Then account should be created successfully
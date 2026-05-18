Feature: Open New Account

  Scenario: Open savings account successfully
    Given user logs into parabank
    When user navigates to open new account page
    And user selects savings account type
    And user clicks on open account button
    Then account should be created successfully
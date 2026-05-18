Feature: Open New Bank Account

  Background:
    Given user launches parabank application
    When user logs in with valid credentials

  Scenario: Open new checking account successfully
    Given user navigates to open new account page
    When user selects "CHECKING" account type
    And user selects existing account for funding
    And clicks on open new account button
    Then new account should be created successfully

  Scenario: Open new savings account successfully
    Given user navigates to open new account page
    When user selects "SAVINGS" account type
    And user selects existing account for funding
    And clicks on open new account button
    Then new account should be created successfully
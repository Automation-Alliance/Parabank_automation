Feature: Accounts Overview Validation

  Background:
    Given user launches parabank application
    When user logs in with valid credentials

  Scenario: Verify account overview details
    Given user navigates to accounts overview page
    Then all customer accounts should be displayed
    And account balance should be visible
    And available balance should be visible
    And total balance should be displayed
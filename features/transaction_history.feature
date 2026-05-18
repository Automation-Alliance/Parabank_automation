Feature: Transaction History Validation

  Scenario: Verify transaction history details
    Given user logs into parabank
    When user navigates to accounts overview page
    Then transaction details should display correctly
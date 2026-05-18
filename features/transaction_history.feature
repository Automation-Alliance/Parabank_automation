Feature: Transaction History Validation

  Scenario: Verify transaction history details
    Given user logs into parabank
    When user navigates to accounts overview page
    And user opens transaction history
    Then transaction details should display correctly
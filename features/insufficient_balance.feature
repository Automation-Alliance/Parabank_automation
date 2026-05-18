Feature: Insufficient Balance Validation

  Scenario: Transfer funds with insufficient balance
    Given user logs into parabank
    When user navigates to transfer funds page
    And user enters transfer amount greater than balance
    And user clicks on transfer button
    Then transfer should fail with insufficient balance message
Feature: Insufficient Balance Validation

  Scenario: Transfer funds with insufficient balance
    Given user logs into parabank
    When user transfers amount greater than account balance
    Then transfer should fail with insufficient balance message
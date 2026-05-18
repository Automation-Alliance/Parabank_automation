Feature: Fund Transfer

  Scenario: Transfer funds successfully
    Given user logs into parabank
    When user transfers amount with sufficient balance
    Then transfer should complete successfully
Feature: Loan Rejection Validation

  Scenario: Apply for loan with invalid details
    Given user logs into parabank
    When user applies for loan with invalid amount
    Then loan request should be rejected
Feature: Loan Request

  Scenario: Apply for loan with valid details
    Given user logs into parabank
    When user applies for loan with valid amount and down payment
    Then loan request should be processed successfully
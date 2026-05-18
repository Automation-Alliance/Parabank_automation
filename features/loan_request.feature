Feature: Loan Request

  Scenario: Apply for loan with valid details
    Given user logs into parabank
    When user navigates to request loan page
    And user enters valid loan amount
    And user enters valid down payment
    And user clicks on apply loan button
    Then loan request should be processed successfully
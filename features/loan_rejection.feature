Feature: Loan Rejection Validation

  Scenario: Apply for loan with invalid details
    Given user logs into parabank
    When user navigates to request loan page
    And user enters invalid loan amount
    And user clicks on apply loan button
    Then loan request should be rejected
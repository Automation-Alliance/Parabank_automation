Feature: Fund Transfer

  Scenario: Transfer funds successfully
    Given user logs into parabank
    When user navigates to transfer funds page
    And user enters valid transfer amount
    And user clicks on transfer button
    Then transfer should complete successfully
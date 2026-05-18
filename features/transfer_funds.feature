Feature: Fund Transfer Functionality

  Background:
    Given user launches parabank application
    When user logs in with valid credentials

  Scenario: Transfer funds successfully
    Given user navigates to transfer funds page
    When user enters valid transfer amount
    And user selects valid sender and receiver accounts
    And clicks on transfer button
    Then transfer should complete successfully

  Scenario: Transfer funds with insufficient balance
    Given user navigates to transfer funds page
    When user enters amount greater than account balance
    And user selects valid sender and receiver accounts
    And clicks on transfer button
    Then transfer should fail with insufficient balance message

  Scenario: Transfer funds with invalid amount
    Given user navigates to transfer funds page
    When user enters invalid transfer amount
    Then appropriate validation message should be displayed

  Scenario: Transfer funds using same sender and receiver account
    Given user navigates to transfer funds page
    When user selects same account for sender and receiver
    And enters valid transfer amount
    Then transfer should not be allowed
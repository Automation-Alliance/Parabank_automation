Feature: Banking User Flow


  Scenario: User Registration
    Given user launches parabank application
    When user clicks on register link
    And user enters valid registration details
    And clicks on register button
    Then user account should be created successfully

  @Login
  Scenario: User Login
    Given user launches parabank application
    When user enters valid username and password
    And clicks on login button
    Then user should navigate to parabank home page

  Scenario: Forgot Login Information
    Given user launches parabank application
    When user clicks on forgot login info link
    And user enters recovery details
    And clicks on find login info button
    Then user should recover login credentials successfully

  @OpenNewAccount
  Scenario: Open New Account
    Given user launches parabank application
    When user enters valid username and password
    And clicks on login button
    And user clicks on open new account link
    And user selects account type
    And user selects existing account
    And user clicks on open new account button
    Then new bank account should be created successfully

  Scenario: Accounts Overview
    Given user launches parabank application
    When user enters valid username and password
    And clicks on login button
    And user clicks on accounts overview link
    Then accounts overview page should display successfully

  @TransferFunds
  Scenario: Transfer Funds
    Given user launches parabank application
    When user enters valid username and password
    And clicks on login button
    And user clicks on transfer funds link
    And user enters transfer amount
    And user selects from account
    And user selects to account
    And user clicks on transfer button
    Then funds should transfer successfully

  Scenario: Bill Pay
    Given user launches parabank application
    When user enters valid username and password
    And clicks on login button
    And user clicks on bill pay link
    And user enters bill pay details
    And user clicks on send payment button
    Then bill payment should complete successfully

  Scenario: Find Transactions
    Given user launches parabank application
    When user enters valid username and password
    And clicks on login button
    And user clicks on find transactions link
    And user enters transaction id
    And user clicks on find transactions button
    Then transaction details should display successfully

  Scenario: Update Contact Info
    Given user launches parabank application
    When user enters valid username and password
    And clicks on login button
    And user clicks on update contact info link
    And user updates contact information
    And user clicks on update profile button
    Then contact information should update successfully

  Scenario: Request Loan
    Given user launches parabank application
    When user enters valid username and password
    And clicks on login button
    And user clicks on request loan link
    And user enters loan details
    And user clicks on apply now button
    Then loan request should submit successfully

  Scenario: Invalid Login
    Given user launches parabank application
    When user enters invalid username and password
    And clicks on login button
    Then invalid login error message should display


  Scenario: Logout
    Given user launches parabank application
    When user enters valid username and password
    And clicks on login button
    And user clicks on logout link
    Then user should logout successfully


# Scenario: Login Screenshot Test

#   Given user launches parabank application
#   When user enters valid username and password
#   And clicks on login button
#   Then user should navigate to parabank home page
Feature: Banking User Flow
   Scenario: Find Transactions
      Given user launches parabank application
      When user enters valid username and password
      And clicks on login button
      And user clicks on find transactions link
      And user enters transaction id
      And user clicks on find transactions button
      Then transaction details should display successfully

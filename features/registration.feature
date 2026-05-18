Feature: Banking User Flow


  Scenario: User Registration

    Given user launches parabank application
    When user clicks on register link
    And user enters valid registration details
    And clicks on register button
    Then user account should be created successfully


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
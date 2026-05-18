Feature: Open New Account

  Scenario: Open savings account successfully
    Given user logs into parabank
    When user opens a new savings account
    Then account should be created successfully
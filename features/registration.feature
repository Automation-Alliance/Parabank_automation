Feature: Registration Functionality

  Scenario: Verify user registration

    Given user opens parabank application
    When user clicks register link
    And user enters registration details
    And user clicks register button
    Then registration should be successful
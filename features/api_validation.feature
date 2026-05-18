Feature: API Validation

  Scenario: Validate loan API response
    Given loan API endpoint is available
    When user sends valid loan request payload
    Then API should return status code 200
    And API response should contain customer data
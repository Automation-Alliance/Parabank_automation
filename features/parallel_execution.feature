Feature: Parallel Execution Validation

  Scenario: Execute multiple workflows in parallel
    Given loan and transfer workflows are configured
    When tests are executed in parallel
    Then all workflows should execute successfully
Feature: Load resume page

  Scenario: Check if the resume page loads
    Given the resume page is loaded
    Then the page title should be "Anthony Coughlin - QA Manager"

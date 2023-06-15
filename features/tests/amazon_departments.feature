# Created by macbookpro at 6/15/23
Feature: Search in departments

  Scenario: User should be able to search for products in any department
    Given User is on Amazon homepage
    When Select computers department
    And Search for 'Macbook'
    Then Verify the correct department is displayed
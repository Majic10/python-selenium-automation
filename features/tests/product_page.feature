# Created by majidtahiri at 5/26/23
Feature: Select product color

  Scenario: User can select any color for a product
    Given I am on Amazon homepage
    When I search for 'T-shirt'
    And Store product name
    And I click on an item
    Then Verify all colors are clickable
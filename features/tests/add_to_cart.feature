# Created by majidtahiri at 5/10/23
Feature: Add items to cart

  Scenario: Add item to cart
    Given I am on Amazon homepage
    When I search for 'Pen'
    And Store the product name
    And I click on an item
    And I click on 'Add to Cart' button
    And I click on 'Go to Cart' button
    Then Verify item(s) added to cart
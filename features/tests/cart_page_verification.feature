# Created by majidtahiri at 5/10/23
Feature: Verify cart page is empty

  Scenario: User navigates to cart page
    Given User is on Amazon homepage
    When User navigates to the cart page
    Then Cart page is displayed with no items in it
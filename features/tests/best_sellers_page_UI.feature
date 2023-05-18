# Created by majidtahiri at 5/14/23
Feature: Verify number of links on Best Sellers page

  Scenario: User should have 5 links on Best Sellers page
    Given User is on Amazon homepage
    When User navigates to best sellers page
    Then Clicked link is displayed
    And 4 links should be displayed on the page
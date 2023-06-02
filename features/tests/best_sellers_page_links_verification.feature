# Created by majidtahiri at 6/1/23
Feature: Best Seller Page Links Verification

  Scenario: User should be able to click on all links on this page
    Given User is on Amazon homepage
    When User navigates to best sellers page
    Then User verifies all links are clickable and open
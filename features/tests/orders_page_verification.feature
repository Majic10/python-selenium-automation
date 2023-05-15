# Created by majidtahiri at 5/10/23
Feature: Verify orders page is opened

  Scenario: User navigates to orders page
    Given User is on Amazon homepage
    When User navigates to the orders page
    Then The sign-in page is displayed
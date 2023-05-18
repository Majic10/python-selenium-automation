# Created by majidtahiri at 5/17/23
Feature: Customer Service Page User Interface Verification

  Scenario: Verify User Interface of Customer Service Page
    Given User is on Amazon homepage
    When User navigates to customer service page
    Then the 'Welcome to Amazon Customer Service' section is displayed
    And User should see a help section
# Created by macbookpro at 6/14/23
Feature: Hover action

  Scenario: View Deals after Hovering over New Arrivals
    Given User is on Amazon homepage
    When Navigates to Amazon Home page
    And Hover over New Arrivals link
    Then Verify deals are displayed
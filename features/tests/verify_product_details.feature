# Created by majidtahiri at 5/27/23
Feature: Product Search

  Scenario: Verify all products on search page have a picture and a name
    Given I am on Amazon homepage
    When I search for 'T-shirt'
    Then verify products have picture and name
    Then Print verification results
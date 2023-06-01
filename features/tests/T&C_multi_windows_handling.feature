# Created by majidtahiri at 5/31/23
  Feature: Handling multiple windows
  Scenario: User should be able to open and close Amazon Privacy Notice
    Given User is on Amazon homepage
    Given User is on the Amazon Terms and Conditions page
    And Store the current window
    When User opens the Amazon Privacy Notice link
    And Switch to the newly opened window
    Then User verifies that the Amazon Privacy Notice page is opened
    And Close the new window
    And Switch back to the original window
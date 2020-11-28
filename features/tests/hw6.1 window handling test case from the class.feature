# Created by ayantknv at 11/23/20
Feature: Create window handling test case from the class

  Scenario: User can open and close Amazon Applications
    Given Open Amazon T&C page
    When Store original windows
    When Click on Amazon applications link
    When Switch to the newly opened window
    Then Amazon app page is opened
    And User can close new window and switch back to original
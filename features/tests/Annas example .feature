# Created by ayantknv at 11/27/20
Feature: Amazon main page

  Scenario: Sign in popup disappears
    Given Open amazon page
    When Sign in popup is present
    And Sign in popup disappears
    Then Verify Sign-in popup is not visible




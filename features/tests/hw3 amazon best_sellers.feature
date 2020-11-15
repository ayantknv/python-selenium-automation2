# Created by ayantknv at 11/11/20
Feature: Amazon best sellers

  Scenario: Verify links in amazon best sellers
    Given Open Amazon page
    When Click on best sellers menu
    Then Verify 1 links on the page

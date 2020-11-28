# Created by ayantknv at 11/24/20
Feature: verifying best sellers link on top of the menu

  Scenario: User can open and close links on the menu
    Given Open amazon best sellers
    Then Click on each top link and verify new page opens

# Created by ayantknv at 12/4/20
Feature: Page object pattern

  Scenario: Amazon Music has 7 menu items
  Given Open Amazon page
  When Click on hamburger menu
  And Click on Amazon Music menu item
  Then 7 menu items are present
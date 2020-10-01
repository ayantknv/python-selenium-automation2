# Created by ayantknv at 9/30/20
Feature: Test for sign in page on Amazon
  # Enter feature description here

  Scenario: Logged out user sees Sign in page when clicking Orders
    Given Open Amazon page
    When Click on Returns & Orders
    Then Sign in page opened
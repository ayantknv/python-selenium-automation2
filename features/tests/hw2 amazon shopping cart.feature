# Created by ayantknv at 10/21/20
Feature: Amazon cart

  Scenario: Amazon returns correct result
    Given Open Amazon page
    When In the search field input face mask
    Then Verify face mask inquiry is shown

  Scenario: Chose second item and add to the shopping cart
    Given Open Amazon page
    When Input face mask on the search field
    When select second product on the list
    And Add the product to the shopping cart
    Then Verify selected product on shopping cart






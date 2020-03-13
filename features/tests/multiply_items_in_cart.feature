# Created by tetyanakuzmyna at 3/5/20
Feature: HomeDepot project

  Scenario: User is able to add multiple items to the Shopping Cart

    Given Open HomeDepot page
    When Insert circular saw in search field
    And On search results page choose something and click it
    And Add product to shopping cart
    And Return to product search page
    And On search results page choose another product and click it
    And Add product to shopping cart
    Then Expected products would be in cart
    And Close all pop-ups
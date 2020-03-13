# Created by tetyanakuzmyna at 3/5/20
Feature: HomeDepot project

  Scenario: Add one of circular saw to cart
    Given Open HomeDepot page
    When Insert circular saw in search field
    And On search results page choose something and click it
    And Add product to shopping cart
    Then Expected product would be in cart
#  Селениум не видит локаторы на POP-UP
    And Close all pop-ups
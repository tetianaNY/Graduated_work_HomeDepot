# Created by tetyanakuzmyna at 3/5/20
Feature: HomeDepot project

  Scenario: Add one of circular saw to cart
    Given Open HomeDepot page
    When Insert circular saw in search field
    And On search results page choose something and click it
    And Add product to shopping cart
# Поменяла местами, закрыть и проверить, тк в iframe только по текущему добавлению показывается, а не сколько в корзине
    Then Close all pop-ups
    And Expected product would be in cart
# Created by tetyanakuzmyna at 3/5/20
Feature: HomeDepot project

  Scenario: Shopping cart - Change quantity
    Given Open HomeDepot page
    When Insert circular saw in search field
    And On search results page choose something and click it
    And Add product to shopping cart
    # Поменяла местами, закрыть и проверить, тк в iframe только по текущему добавлению показывается, а не сколько в корзине
    Then Close all pop-ups
    And Expected product would be in cart
    And Click cart button
    And Change quantity from 1 to 2
    And Expected items in cart will be 2
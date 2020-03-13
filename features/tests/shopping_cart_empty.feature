# Created by tetyanakuzmyna at 3/5/20
Feature: HomeDepot project

  Scenario: Shopping cart - empty state
    Given Open HomeDepot page
    When Click HomeDepot cart button
    Then Expected cart page will have empty in the title
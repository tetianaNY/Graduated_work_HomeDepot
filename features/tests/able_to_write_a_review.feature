# Created by tetyanakuzmyna at 3/5/20
Feature: HomeDepot project

  Scenario: User is able to write a review
    Given Open HomeDepot page
    When Insert hammer in search field
    And Click search button or click enter button
    And On search results page choose something and click it
    Then Expected product has "write review" button
# Created by tetyanakuzmyna at 3/5/20
Feature: HomeDepot project

  Scenario: User is taken to the search results page
    Given Open HomeDepot page
    When Insert dry vacuum in search field
    And Click search button or click enter button
    Then Expect to see the search results page. Check that title is relevant to "dry vacuum"
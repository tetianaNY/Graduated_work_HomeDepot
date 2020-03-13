# Created by tetyanakuzmyna at 3/5/20
Feature: HomeDepot project


  Scenario Outline: Verify that Auto-suggestion works
    Examples:
    |search_word      |
    |hammer           |
    |plier            |
    |pry bar          |
    |lawn mower       |


    Given Open HomeDepot page
    When Enter <search_word> to the search box
    Then Count <search_word> on the page
# Created by tetyanakuzmyna at 3/5/20
Feature: HomeDepot project

  Scenario: Verify that Registration flow works as expected
    Given Open HomeDepot page
    When Click account button
    And Click "register" button
    And Fill all fields with fake data
    And Click submit registration form
    Then Expected registration will be complete successfully
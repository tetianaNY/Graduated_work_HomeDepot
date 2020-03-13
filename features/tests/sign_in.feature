# Created by tetyanakuzmyna at 3/5/20
Feature: HomeDepot project

  Scenario: Verify that Sign-In with existing account works
    Given Open HomeDepot page
    When Click account button
    And Fill data from prev step
    And Click sign_in button
    Then Expected login will be complete successfully
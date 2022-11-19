Feature: Login action on gmail page
  Scenario: Login with valid credentials
    Given User is on home page
    When User navigates to login page
    And User enters user as "bddtester2022" and password as "!234567*"
    Then Title of the page displayed is "Google Account"


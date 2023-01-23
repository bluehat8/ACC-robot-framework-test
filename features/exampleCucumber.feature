Feature: Logging in with valid crendentials

Scenario: User login successfully

    Given I create a new User
    When I type User 'usuario'
    When I type password 'password'
    When I click on 'login'
    Then I should see the text welcome

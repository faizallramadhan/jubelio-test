Feature: Login

    Scenario: Login success
    Given I am on the login page
    When I enter valid "Email" and "Password" with the following data:
    | Email | Password |
    | testingwithfai@gmail.com | 123Faizal! | 
    And I click on the login button
    Then I should see an error message
    And screenshot automatically taken
    And Assert with "Password atau email anda salah." text in anywhere in page_source
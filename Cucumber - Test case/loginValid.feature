Feature: Login

    Scenario: Login success
    Given I am on the login page
    When I enter valid "Email" and "Password" with the following data:
    | Email | Password |
    |qa.rakamin.jubelio@gmail.com| Jubelio123! | 
    And I click on the login button
    Then I should be redirected to the dashboard
    And screenshot automatically taken
    And Assert with "Selamat Datang" text in Tittle
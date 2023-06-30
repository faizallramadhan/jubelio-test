Feature: Edit stock

    Scenario: Add stock success
    Given I am logged in successfully
    And I am in dashboard page
    When I click on "Barang"
    Then Sub menu "Barang" should appear
    When I click on "Persediaan"
    Then I should be redirected to "Persediaan" page
    When I click on "Penyesuaian Persediaan"
    Then I should be redirected to "Penyesuaian Persediaan" page
    When I enter "Scan" value with the following data:
    | Scan |
    | MAM2 |
    And I click on scan button
    Then product with code MAM2 should appeared
    When I click on "Simpan" button
    Then I should see notification
    And the product "Qty" should be increased

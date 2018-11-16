Feature: Transfer between accounts

    Given I have 10.000€ in my current acount
    And I have 300€ in my saving accout
    When I transfer 200€ from current to saving
    Then I should have 9.800€ in my current acount
    And I should have 500€ in my saving acount

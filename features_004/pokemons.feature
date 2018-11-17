Feature: Pokemon search 

  Scenario: Find the weakest

    Given I have this pokemons
        |name     | attack  | defense |
        |psyduck  | 20      | 60      |
        |torchic  | 20      | 60      |
        |spinda   | 10      | 80      |
        |lillipup | 10      | 50      |
    When I search for the one with less defense
    Then I should get lillipup

Feature: Search pokemons

  Background:
        
    Given I have this pokemons
        |name     | attack  | defense |
        |psyduck  | 20      | 60      |
        |torchic  | 20      | 60      |
        |trapinch | 20      | 60      |
        |spinda   | 10      | 80      |
        |lillipup | 10      | 50      |

  @fight
  Scenario: Search for the weakest 
    When I search for the one with less defense
    Then I should get lillipup

  @fight
  Scenario: Search for the stronger
    When I search for the one with more attack
    Then I should get spinda

  Scenario: Search for name 
    When I search for the letter t
    Then I should get torchic
     And I should get trapinch

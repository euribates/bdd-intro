Feature: Pokemom attack

 Scenario: Psyduck attacks Torchic

    Given pokemon Torchic with 20 attack
    And pokemon Psyduck with 60 defense
    When Torchic attacks Psyduck
    Then defense of Psyduck goes down to 40


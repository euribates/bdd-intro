#!/usr/bin/env python

class Pokemon:

    registry = dict()

    def __init__(self, name, attack=10, defense=10):
        if name in Pokemon.registry:
            self = Pokemon.registry[name]
        else:
            self.name = name
            self.attack = attack
            self.defense = defense
            Pokemon.registry[name] = self


    def __str__(self):
        return self.name


    @classmethod
    def find(cls, name):
        return cls.registry.get(name, None)

    @classmethod
    def find_weakest(cls):
        return min(
            cls.registry.values(),
            key=lambda x: x.defense
            ) if cls.registry else None

    @classmethod
    def find_strongest(cls):
        return max(
            cls.registry.values(),
            key=lambda x: x.defense
            ) if cls.registry else None

    @classmethod
    def find_by_name(cls, name):
        return [
            p for p in cls.registry.values()
            if name in p.name
            ]

def attack(attacker, defender):
    defender.defense -= attacker.attack

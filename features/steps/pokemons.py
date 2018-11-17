import pytest
from behave import *
from models import Pokemon, attack

@given('pokemon {name} with {attack:d} attack')
def step_impl(context, name, attack):
    setattr(context, name, Pokemon(name, attack=attack))


@given('pokemon {name} with {defense:d} defense')
def step_impl(context, name, defense):
    setattr(context, name, Pokemon(name, defense=defense))


@when('{attacker} attacks {defender}')
def step_impl(context, attacker, defender):
    a = getattr(context, attacker)
    d = getattr(context, defender)
    attack(a, d)
    

@then('defense of {name} goes down to 40')
def step_impl(context, name):
    p = getattr(context, name)
    assert p.defense == 40


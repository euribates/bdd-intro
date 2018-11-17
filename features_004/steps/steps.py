import pytest
from behave import *
from models import Pokemon

@given('I have this pokemons')
def step_impl(context):
    for row in context.table:
        pokemon = Pokemon(
            row['name'],
            attack=row['attack'],
            defense=row['defense'],
            )
        setattr(context, row['name'], pokemon)


@when('I search for the one with less defense')
def step_impl(context):
    context.target = Pokemon.find_weakest()

@then('I should get {name}')
def step_impl(context, name):
    assert context.target.name == name

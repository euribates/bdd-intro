#!/usr/bin/env python

from behave import *

@given("I have {amount}€ in my current acount")
def step_impl(context, amount):
    context.current_account = int(amount)


@given("I have 300€ in my saving accout")
def step_impl(context):
    context.savings_account = 300


@when("I transfer 200€ from current to saving")
def step_impl(context):
    context.savings_account += 200
    context.current_account -= 200


@then("I should have 9800€ in my current acount")
def step_impl(context):
    assert context.current_account == 9800

@then("I should have 500€ in my saving acount")
def step_impl(context):
    assert context.savings_account == 500

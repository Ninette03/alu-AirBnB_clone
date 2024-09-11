#!/usr/bin/python3
""" State class """

from models.base_model import BaseModel


class State(BaseModel):
    """ State class """
    name = ""


state1 = State()
state1.name = "California"

state2 = State()
state2.name = "New York"

# Print state information
print(state1.__dict__)
print(state2.__dict__)

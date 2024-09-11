#!/usr/bin/python3
""" City class """

from models.base_model import BaseModel


class City(BaseModel):
    """ City class """
    state_id = ""
    name = ""


city1 = City()
city1.state_id = 567
city1.name = "New York City"
city2 = City()
city2.state_id = 345
city2.name = "San Francisco"

print(city1.__dict__)
print(city2.__dict__)

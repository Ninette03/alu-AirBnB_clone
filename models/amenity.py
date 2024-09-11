#!/usr/bin/python3
"""Amenity class"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """Amenity class"""
    name = ""


amenity1 = Amenity()
amenity1.name = "Wi-Fi"

amenity2 = Amenity()
amenity2.name = "Swimming Pool"

print(amenity1.__dict__)
print(amenity2.__dict__)

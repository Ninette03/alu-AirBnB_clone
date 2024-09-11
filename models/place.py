#!/usr/bin/python3
""" Place class """

from models.base_model import BaseModel


class Place(BaseModel):
    """ Place class """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []


place1 = Place()
place1.city_id = "city123"
place1.user_id = "user456"
place1.name = "Cozy Cottage"
place1.description = "A charming cottage in the countryside"
place1.number_rooms = 2
place1.number_bathrooms = 1
place1.max_guest = 4
place1.price_by_night = 100
place1.latitude = 37.7749
place1.longitude = -122.4194

place2 = Place()
place2.city_id = "city789"
place2.user_id = "user101"
place2.name = "Urban Loft"
place2.description = "Modern loft in the heart of the city"
place2.number_rooms = 1
place2.number_bathrooms = 1
place2.max_guest = 2
place2.price_by_night = 150
place2.latitude = 40.7128
place2.longitude = -74.0060

print(place1.__dict__)
print(place2.__dict__)

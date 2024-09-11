#!/usr/bin/python3
""" Review class """

from models.base_model import BaseModel


class Review(BaseModel):
    """ Review class """
    place_id = ""
    user_id = ""
    text = ""


# Create Review instances
review1 = Review()
review1.place_id = "place123"
review1.user_id = "user456"
review1.text = "Great experience, highly recommended!"

review2 = Review()
review2.place_id = "place789"
review2.user_id = "user101"
review2.text = "Average stay, could be improved."

# Print review information
print(review1.__dict__)
print(review2.__dict__)

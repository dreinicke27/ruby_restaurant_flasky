from flask import Blueprint, jsonify

class Restaurant:
    def __init__(self, id, rating, name, cuisine, distance_from_ada):
        self.id = id
        self.rating = rating
        self.name = name
        self.cuisine = cuisine
        self.distance_from_ada = distance_from_ada

restaurant1 = Restaurant(1, 5, "Pizza Hut", "Italian", 3.6)
restaurant2 = Restaurant(15, 2, "Dominos", "American", 0.2)
restaurant3 = Restaurant(9, 4.5, "Hong Kong Bistro", "Chinese", 0.1)

restaurant_list = [restaurant1, restaurant2, restaurant3]

restaurant_bp = Blueprint("restaurant", __name__, url_prefix="/restaurant")

@restaurant_bp.route("", methods=["GET"])
def get_restaurants():
    response = []
    for restaurant in restaurant_list: 
        restaurant_dict = {
            "id": restaurant.id,
            "rating": restaurant.rating,
            "name": restaurant.name,
            "cuisine": restaurant.cuisine,
            "distance_from_ada": restaurant.distance_from_ada 
        }
        response.append(restaurant_dict)

    return jsonify(response), 200
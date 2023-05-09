from app import db

class Restaurant(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    rating = db.Column(db.Integer)
    name = db.Column(db.String)
    cuisine = db.Column(db.String)
    distance_from_ada = db.Column(db.Integer)
    employees = db.relationship("Employee", back_populates="restaurant")

    def to_dict(self):
        #employees = [employee.to_dict() for employee in self.employees]
        return {
                "id": self.id,
                "rating": self.rating,
                "name": self.name,
                "cuisine": self.cuisine,
                "distance_from_ada": self.distance_from_ada 
                #"employees": employees
        }
    
    # class method lets you call it on the general class, before an instance is creaeted
    @classmethod
    def from_dict(cls, restaurant_data):
        #use cls so that child class could use this method correctly 
        return cls(
            rating = restaurant_data["rating"],
            name = restaurant_data["name"],
            cuisine = restaurant_data["cuisine"],
            distance_from_ada = restaurant_data["distance_from_ada"]
        )
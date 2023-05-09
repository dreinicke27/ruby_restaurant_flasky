import pytest

# test that we can accurately get all restaurants
# client fixture simulates hitting our test client, two_restaurants fixture sets up db
def test_get_all_restaurants(client, two_restaurants):
    response = client.get("/restaurant")
    response_body = response.get_json()
    
    assert response.status_code == 200
    assert response_body == [{
        "id": 1,
        "cuisine": "Italian",
        "distance_from_ada": 15,
        "name": "Olive Garden",
        "rating": 5 
        
    }, {
        "id": 2,
        "cuisine": "American",
        "distance_from_ada": 46,
        "name": "Texas Roadhouse",
        "rating": 3
    }]
    # can only call fixtures as args of the function, not in the body 

def test_post_creates_restaurant(client):
    response = client.post("/restaurant", json={
        "cuisine": "Italian",
        "distance_from_ada": 15,
        "name": "Olive Garden",
        "rating": 5
    })

    response_body = response.get_json()

    assert response.status_code == 201
    assert "id" in response_body

def test_delete_removes_restaurant(client, two_restaurants):
    response = client.delete("/restaurant/2")
    response_body = response.get_json()

    assert response.status_code == 200
    assert "Restaurant 2 successfully deleted" in response_body["msg"]

def test_put_updates_restaurant(client, two_restaurants):
    response = client.put("/restaurant/1", json={
        "cuisine": "Filipino",
        "distance_from_ada": 1,
        "name": "Hood Famous",
        "rating": 5
    })
    response_body = response.get_json()

    assert response.status_code == 200
    assert "Restaurant 1 successfully updated" in response_body["msg"]
    # because put route only has this as a success message, can't check more specifically 
    # could consider returning something else, so we'd have more info 
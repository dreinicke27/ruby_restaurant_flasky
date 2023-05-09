import pytest
from app import create_app, db #db is the SQLAlchemy object defined in app.__init__
from flask.signals import request_finished
from app.models.restaurant import Restaurant

@pytest.fixture
def app():
    app = create_app(testing=True)

    # this line lets flask call the expire session function
    # this function cleans up after each request  
    @request_finished.connect_via(app)
    def expire_session(sender, response, **extra):
        db.session.remove()

    #need access to app context outside of regularly defined routes
    with app.app_context():
        #set up 
        db.create_all()
        #pause to do the stuff after set up (running a test)
        yield app
        #tear down
        db.drop_all()

@pytest.fixture
def client(app):
    #set up a test client
    return app.test_client()

@pytest.fixture
def two_restaurants():
    olivegarden = Restaurant(name="Olive Garden",cuisine="Italian",rating=5,distance_from_ada=15)
    texasroadhouse = Restaurant(name="Texas Roadhouse",cuisine="American",rating=3,distance_from_ada=46)

    db.session.add_all([olivegarden, texasroadhouse])
    db.session.commit()


from problem2 import app, db, Signup
import pytest


@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    client = app.test_client()

    with app.app_context():
        db.create_all()

    yield client  # return the client and drop the database afterwards, this is where the test happens

    with app.app_context():
        db.drop_all()


def test_index(client):
    response = client.post(
        '/', data={'student_name': 'Noella', 'course_name': 'Python Programming'})

    with app.app_context():
        signups = Signup.query.all()
        assert len(signups) == 1
        assert signups[0].student_name == 'Noella'
        assert signups[0].course_name == 'Python Programming'


def test_cancel(client):
    # Create a new item for test deletion
    response = client.post(
        '/', data={'student_name': 'Alice', 'course_name': 'Web Development'})

    with app.app_context():
        signups_before_cancel = Signup.query.all()
        assert len(signups_before_cancel) == 1
        signup_id = signups_before_cancel[0].id

    response = client.post(f'/cancel/{signup_id}')

    with app.app_context():
        signups_after_cancel = Signup.query.all()
        assert len(signups_after_cancel) == 0

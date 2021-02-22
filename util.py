from flask.ext.testing import TestCase

from project import app, db
from project.models import User

class BaseTest(TestCase):
    def create_app(self):
        app.config.from_object('project.config.TestingConfig')
        return app

    def setUp(self):
        db.create_all()
        user = User(email="ad@min.com", password="admin_user", paid=False)
        db.session.add(user)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
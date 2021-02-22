from flask.ext.testing import TestCase

from project import app, db
from project.models import User

class BaseTest(TestCase):
    def create_app(self):
        app.config.from_object('project.config.TestingConfig')
        return app
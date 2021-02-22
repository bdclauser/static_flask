import os
import unittest
import coverage

from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand

import app
import db
import User

app.config.from_object(os.environ['APP_SETTINGS'])

migrate = Migrate(app, db)
mananger = Manager(app)

# migrations
manager.add_command('db', MigrateCommand)


@manager.command
def test():
    """Runs the unit test without coverage."""
    tests = unittest.TestLoader().discover('tests')
    results = unittest.TextTextRunner(verbosity=2).run(tests)
    if results.wasSuccessful():
        return 0
    else:
        return 1


@manager.command
def cov():
    """Runs the unti tests with coverage."""
    cov = covereage.coverage(branch=True, include="project/*")

    # TODO: Need to update branch path

    cov.start()
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)
    cov.stop()
    cov.save()
    print('Coverage Summary')
    cov.report()
    basdir = os.path.abspath(os.path.dirname(__file__))
    covdir = os.path.join(basedir, 'tmp/coverage')
    cov.html_report(directory=covdir)
    print('HTML version; file://%s/index.html' % covdir)
    cov.erase()


@manager.command
def create_db():
    """Creates the db tables.
    """
    db.create_all()


@manager.command
def drop_db():
    """Drops the table, you know that one thing they said never to do..."""
    db.drop_all()
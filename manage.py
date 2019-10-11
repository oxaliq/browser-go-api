import os
import unittest

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from database import db
from app import create_app
app = create_app()

migrate = Migrate(app, db)
manager = Manager(app)

from models.Game import Game
from models.GameRoom import GameRoom
from models.Message import Message
from models.Move import Move
from models.User import User

# migrations
manager.add_command('db', MigrateCommand)


@manager.command
def test():
    """Runs the unit tests without test coverage."""
    tests = unittest.TestLoader().discover('browser-go-api/tests', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1


@manager.command
def create_db():
    """Creates the db tables."""
    db.create_all()


@manager.command
def drop_db():
    """Drops the db tables."""
    db.drop_all()


if __name__ == '__main__':
    manager.run()
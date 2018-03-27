from flask_script import Manager
from src.server import app

manager = Manager(app)


@manager.command
def test():
    import unittest
    suite = unittest.TestLoader().discover("tests", pattern="*.py")
    unittest.TextTestRunner().run(suite)


if __name__ == "__main__":
    manager.run()

from app import create_app
from flask_script import Manager
from config import config

app = create_app(config['development'])
manager = Manager(app)

if __name__ == "__main__":
    manager.run()
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from src.app import create_simple_app
from src.models import db

app = create_simple_app()
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()

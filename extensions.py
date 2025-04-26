
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_frozen import Freezer

db = SQLAlchemy()
migrate = Migrate()
freezer = Freezer()

def init_extensions(app):
    db.init_app(app)
    migrate.init_app(app, db)

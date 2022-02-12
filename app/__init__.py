from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
import os
from flask_cors import CORS

db = SQLAlchemy()
migrate = Migrate()
load_dotenv()


def create_app(test_config=None):
    app = Flask(__name__)
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get(
        "SQLALCHEMY_DATABASE_URI")

    from app.models.user import User
    from app.models.project import Project
    # from app.models.collaborator import Collaborator

    db.init_app(app)
    migrate.init_app(app, db)

    # Register Blueprints
    from .routes import user, project
    # (removed from above) collaborator
    app.register_blueprint(user.bp)
    app.register_blueprint(project.bp)
    # app.register_blueprint(collaborator.bp)


    CORS(app)
    return app

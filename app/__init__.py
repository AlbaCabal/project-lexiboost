from flask import Flask
from flask_session import Session
from dotenv import load_dotenv
import os
from app.extensions import db
from app.routes.auth_routes import auth_bp
from app.routes.content_routes import content_bp


def create_app(test_config=None):
    load_dotenv()
    app = Flask(__name__)
    app.secret_key = os.getenv("SECRET_KEY")

    app.config["SESSION_PERMANENT"] = False
    app.config["SESSION_TYPE"] = "filesystem"
    Session(app)

    user = os.getenv("USER_BD")
    password = os.getenv("PASS_BD")
    host = os.getenv("HOST_BD")
    database = os.getenv("NAME_BD")

    app.config["SQLALCHEMY_DATABASE_URI"] = (
        f"mysql+pymysql://{user}:{password}@{host}/{database}"
    )
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    if test_config:
        app.config.update(test_config)

    db.init_app(app)

    app.register_blueprint(auth_bp)
    app.register_blueprint(content_bp)

    @app.after_request
    def after_request(response):
        response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
        response.headers["Expires"] = 0
        response.headers["Pragma"] = "no-cache"
        return response

    return app


if __name__ == "__main__":
    app = create_app()
    debug = os.getenv("FLASK_DEBUG", "false").lower() == "true"
    app.run(debug=debug)
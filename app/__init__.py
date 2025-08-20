from flask import Flask
from app.config import Config
from app.extensions import db, migrate
from flask_cors import CORS


def create_app():
    app = Flask(__name__)

    # Configurações
    app.config.from_object(Config)

    # Inicializa extensões
    db.init_app(app)
    migrate.init_app(app, db)

    # Habilita CORS para permitir chamadas do front
    CORS(app)

    # Importa rotas
    from app.controllers.investment_controller import investment_bp
    app.register_blueprint(investment_bp, url_prefix="/investments")

    @app.route("/")
    def index():
        return {"message": "API de Investimentos está rodando"}

    return app

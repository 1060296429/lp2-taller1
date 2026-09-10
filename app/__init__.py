"""
Application factory de la Tienda Virtual.

Este patrón (application factory) es una buena práctica en Flask porque
permite crear la app de forma controlada, registrar rutas/blueprints,
y facilita las pruebas automatizadas más adelante.
"""

from flask import Flask


def create_app():
    """Crea y configura la instancia de la aplicación Flask."""
    app = Flask(__name__)

    # TODO 1: Importar el Blueprint 'main' desde app/routes.py
    # from .routes import main

    # TODO 2: Registrar el blueprint en la aplicación
    # app.register_blueprint(main)

    return app

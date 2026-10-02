import os

from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS
from dotenv import load_dotenv

from services.password_analyzer import analyze_password
from services.password_generator import generate_password


load_dotenv()


BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

FRONTEND_DIR = os.path.join(
    BASE_DIR,
    "frontend"
)


def create_app():

    app = Flask(
        __name__,
        static_folder=FRONTEND_DIR,
        static_url_path=""
    )

    CORS(app)

    app.config["SECRET_KEY"] = os.getenv(
        "SECRET_KEY",
        "development-only-key"
    )

    # -------------------------
    # Frontend
    # -------------------------

    @app.get("/")
    def index():

        return send_from_directory(
            FRONTEND_DIR,
            "index.html"
        )

    @app.get("/dashboard")
    def dashboard():

        return send_from_directory(
            FRONTEND_DIR,
            "dashboard.html"
        )

    # -------------------------
    # Analyze password
    # -------------------------

    @app.post("/api/analyze")
    def analyze():

        data = request.get_json(
            silent=True
        ) or {}

        password = data.get(
            "password",
            ""
        )

        if not isinstance(password, str):
            return jsonify({
                "error": "Invalid password input."
            }), 400

        if len(password) > 256:
            return jsonify({
                "error": "Password exceeds supported length."
            }), 400

        context = data.get(
            "context",
            {}
        )

        if not isinstance(context, dict):
            context = {}

        result = analyze_password(
            password,
            context
        )

        # IMPORTANT:
        # Password is never returned,
        # logged, or stored.

        return jsonify(result)

    # -------------------------
    # Generate password
    # -------------------------

    @app.post("/api/generate-password")
    def generate():

        data = request.get_json(
            silent=True
        ) or {}

        length = data.get(
            "length",
            20
        )

        try:
            length = int(length)
        except (ValueError, TypeError):

            return jsonify({
                "error": "Invalid length."
            }), 400

        length = min(
            max(length, 12),
            128
        )

        try:

            password = generate_password(
                length=length,
                use_uppercase=data.get(
                    "uppercase",
                    True
                ),
                use_lowercase=data.get(
                    "lowercase",
                    True
                ),
                use_numbers=data.get(
                    "numbers",
                    True
                ),
                use_symbols=data.get(
                    "symbols",
                    True
                )
            )

        except ValueError as error:

            return jsonify({
                "error": str(error)
            }), 400

        return jsonify({
            "password": password
        })

    return app


app = create_app()


if __name__ == "__main__":

    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True
    )
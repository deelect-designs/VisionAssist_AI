
from flask import Flask, render_template, jsonify
from config import Config


def create_app():
    app = Flask(__name__)

    # Load application settings
    app.config.from_object(Config)

    # Homepage
    @app.route("/")
    def home():
        return render_template("index.html")

    # Health check
    @app.route("/health")
    def health():
        return jsonify({
            "status": "healthy",
            "application": "VisionAssist AI",
            "message": "Application is running successfully."
        }), 200

    # About the application
    @app.route("/about")
    def about():
        return jsonify({
            "name": "VisionAssist AI",
            "purpose": (
                "An AI-powered accessibility platform "
                "for people who are blind or have low vision."
            ),
            "version": "0.1.0"
        }), 200

    return app


app = create_app()


if __name__ == "__main__":
    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True
    )

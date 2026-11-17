
import os


class Config:
    APP_NAME = "VisionAssist AI"

    SECRET_KEY = os.environ.get(
        "SECRET_KEY",
        "development-key-change-before-deployment"
    )

    MAX_CONTENT_LENGTH = 10 * 1024 * 1024

    DEBUG = os.environ.get(
        "FLASK_DEBUG",
        "false"
    ).lower() == "true"

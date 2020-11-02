import os


class Config:
    API_ID = int(os.environ.get("1597604"))
    API_HASH = os.environ.get("afa675e093d83bd9023b00f766f69caf")
    AUTH_USERS = set(int(x) for x in os.environ.get("1176240952", "").split())
    BOT_TOKEN = os.environ.get("1440835989:AAGNNkonAwkSflUc6jYsYZwQC-92HNJ24ok")
    DB_URI = os.environ.get("DATABASE_URL")
    SESSION_NAME = os.environ.get("SESSION_NAME")
    WORKERS = 200

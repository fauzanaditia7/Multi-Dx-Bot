import os


class Config:
    API_ID = int(os.environ.get("1597604"))
    API_HASH = os.environ.get("afa675e093d83bd9023b00f766f69caf")
    AUTH_USERS = set(int(x) for x in os.environ.get("1176240952", "").split())
    BOT_TOKEN = os.environ.get("1440835989:AAGNNkonAwkSflUc6jYsYZwQC-92HNJ24ok")
    DB_URI = os.environ.get("postgres://eeerodafkabyyv:2d96adc4bf9ce64eca748d8266acf3f456a591d65a2726c84d22193941c37ce7@ec2-54-75-150-32.eu-west-1.compute.amazonaws.com:5432/d6cgmn1ru4jm8c")
    SESSION_NAME = os.environ.get("SESSION_NAME")
    WORKERS = 200

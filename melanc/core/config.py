from os import environ as env
from pathlib import Path

ROOT_PATH = Path(__file__).resolve(strict=True).parent.parent.parent
STAGE = env.get("MELANC_STAGE", "development")

POSTGRES_DB = env.get("POSTGRES_DB", "melanc_development")
POSTGRES_HOST = env.get("POSTGRES_HOST", "localhost")
POSTGRES_PORT = env.get("POSTGRES_PORT", 5432)
POSTGRES_USER = env.get("POSTGRES_USER", "dean")
POSTGRES_PASSWORD = env.get("POSTGRES_PASSWORD", "dean")

SQLALCHEMY_DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"

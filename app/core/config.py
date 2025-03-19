import os
from pathlib import Path

from dotenv import load_dotenv

dotenv_path = Path(__file__).parent.joinpath(".env")
load_dotenv(dotenv_path)

DB_URL = os.getenv("DB_URL")
DB_ECHO = False
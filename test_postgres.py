from sqlalchemy import create_engine, text
import urllib.parse

DB_USER = "postgres"
DB_PASS = "India123"
DB_NAME = "todolist"
DB_HOST = "127.0.0.1"  # force IPv4
DB_PORT = "5432"

encoded_pass = urllib.parse.quote_plus(DB_PASS)
db_uri = f"postgresql+psycopg2://{DB_USER}:{encoded_pass}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

print("Trying:", db_uri)

engine = create_engine(db_uri)

with engine.connect() as conn:
    print("✅ Connected:", conn.execute(text("SELECT version();")).scalar())

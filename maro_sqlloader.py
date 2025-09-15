# maro_sqlloader.py

# @title Set Your Values Here { display-mode: "form" }
DB_NAME = "todolist"
DB_USER = "postgres"
DB_PASS = "India123"   # your actual password
DB_HOST = "127.0.0.1"  # force IPv4 to avoid IPv6 auth issues
DB_PORT = "5432"
TABLE_NAME = "public.messages"

import urllib.parse
from sqlalchemy import create_engine, text
from langchain_community.utilities import SQLDatabase
from langchain_community.document_loaders.sql_database import SQLDatabaseLoader

def search():
    # URL-encode the password (necessary if it has special chars)
    encoded_pass = urllib.parse.quote_plus(DB_PASS)
    db_uri = f"postgresql+psycopg2://{DB_USER}:{encoded_pass}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    print("Trying:", db_uri)

    # Test connection
    engine = create_engine(db_uri)
    with engine.connect() as conn:
        print("✅ Connected:", conn.execute(text("SELECT version();")).scalar())

    # LangChain SQL loader
    db = SQLDatabase.from_uri(db_uri)
    loader = SQLDatabaseLoader(db, f"SELECT * FROM {TABLE_NAME}")

    # Use synchronous load to avoid async complications
    docs = loader.load()
    print("📄 Docs loaded:", docs)


    search()

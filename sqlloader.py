import sqlalchemy
from sqlalchemy import text
from Message import Message  # your message class

# Local Postgres configuration
DB_USER = "postgres"
DB_PASS = "India123"  # your local Postgres password
DB_NAME = "todolist"  # your database name
DB_HOST = "127.0.0.1"
DB_PORT = "5432"


def connect_local_postgres() -> sqlalchemy.engine.Engine:
    """Creates a SQLAlchemy engine connected to local Postgres."""
    db_uri = f"postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    engine = sqlalchemy.create_engine(db_uri)
    return engine


def get_all_messages_for_user(user: str):
    """Fetch messages for a specific user."""
    select_stmt = text(
        f"SELECT text FROM public.messages WHERE receiver = :user ORDER BY priority, ts LIMIT 1000;"
    )
    engine = connect_local_postgres()
    with engine.connect() as conn:
        result = conn.execute(select_stmt, {"user": user})
        return result.fetchall()  # returns a list of rows


def save_message_for_user(message: Message, user: str):
    """Save a message for a user."""
    insert_stmt = text(
        "INSERT INTO public.messages (text, ts, priority, receiver, sender) "
        "VALUES (:text, :ts, :priority, :receiver, :sender)"
    )
    engine = connect_local_postgres()
    with engine.connect() as conn:
        conn.execute(
            insert_stmt,
            {
                "text": message.text,
                "ts": message.ts,
                "priority": message.priority,
                "receiver": user,
                "sender": message.user,
            },
        )
        conn.commit()

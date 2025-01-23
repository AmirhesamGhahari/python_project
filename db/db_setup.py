from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Float, TIMESTAMP

DATABASE_URL = "postgresql://myuser:mypassword@localhost/mydatabase"

def setup_database():
    engine = create_engine(DATABASE_URL)
    metadata = MetaData()

    # Define table structure
    live_data = Table(
        "live_data",
        metadata,
        Column("id", Integer, primary_key=True, autoincrement=True),
        Column("title", String),
        Column("value", Float),
        Column("timestamp", TIMESTAMP),
    )

    # Create table
    metadata.create_all(engine)

if __name__ == "__main__":
    setup_database()
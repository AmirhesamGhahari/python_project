from sqlalchemy import create_engine
import pandas as pd

# Database connection string
DATABASE_URL = "postgresql://myuser:mypassword@localhost/mydatabase"

def load_data_to_db(data):
    engine = create_engine(DATABASE_URL)
    with engine.connect() as connection:
        data.to_sql("live_data", con=connection, if_exists="append", index=False)
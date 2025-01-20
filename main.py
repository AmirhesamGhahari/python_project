from etl.extract import fetch_live_data
from etl.transform import transform_data
from etl.load import load_data_to_db

def main():
    url = "https://example.com/live-data"
    raw_data = fetch_live_data(url)
    transformed_data = transform_data(raw_data)
    load_data_to_db(transformed_data)
    print("ETL process completed successfully!")

if __name__ == "__main__":
    main()
import requests
from src.database.db_connection import get_db_connection
from src.etl.base_etl import DataETL

class GoogleTrendsETL(DataETL):
    def __init__(self, api_key):
        super().__init__("Google Trends")
        self.api_key = api_key

    def extract(self):
        """Fetch trending data from Google Trends."""
        url = f"https://trends.googleapis.com/api/trending?key={self.api_key}"
        response = requests.get(url)
        response.raise_for_status()
        return response.json()

    def transform(self, data):
        """Transform the raw JSON data into a clean format."""
        transformed_data = []
        for trend in data.get("trendingSearchesDays", []):
            for search in trend.get("trendingSearches", []):
                transformed_data.append({
                    "query": search["title"]["query"],
                    "traffic": search.get("formattedTraffic", "Unknown"),
                    "date": trend["date"]
                })
        return transformed_data

    def load(self, transformed_data):
        """Load the transformed data into PostgreSQL."""
        conn = get_db_connection()
        try:
            with conn.cursor() as cur:
                for row in transformed_data:
                    cur.execute("""
                        INSERT INTO google_trends (query, traffic, date)
                        VALUES (%s, %s, %s)
                        ON CONFLICT (query, date) DO NOTHING
                    """, (row["query"], row["traffic"], row["date"]))
            conn.commit()
        finally:
            conn.close()
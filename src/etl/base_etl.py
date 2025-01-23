from abc import ABC, abstractmethod
from src.utils.logger import get_logger

logger = get_logger(__name__)

class DataETL(ABC):
    def __init__(self, source_name):
        self.source_name = source_name

    @abstractmethod
    def extract(self):
        """Extract data from the source"""
        pass

    @abstractmethod
    def transform(self, data):
        """Transform the extracted data"""
        pass

    @abstractmethod
    def load(self, transformed_data):
        """Load the transformed data into the database"""
        pass

    def run(self):
        """Run the full ETL process"""
        logger.info(f"Starting ETL process for {self.source_name}")
        try:
            data = self.extract()
            transformed_data = self.transform(data)
            self.load(transformed_data)
            logger.info(f"ETL process for {self.source_name} completed successfully.")
        except Exception as e:
            logger.error(f"ETL process for {self.source_name} failed: {e}")
            raise
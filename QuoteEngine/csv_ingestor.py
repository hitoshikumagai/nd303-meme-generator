from typing import List
import pandas as pd
from .ingestor_interface import IngestorInterface
from .quote_model import QuoteModel

class CSVIngestor(IngestorInterface):
    """Ingestor for CSV files."""

    allowed_extensions = ['csv']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse CSV file and return quotes.

        Args:
            path: Path to CSV file

        Returns:
            List[QuoteModel]: List of parsed quotes
        """
        if not cls.can_ingest(path):
            raise Exception('Cannot ingest this file type')
        try:

            quotes = []
            df = pd.read_csv(path)

            for _, row in df.iterrows():
                quotes.append(QuoteModel(row['body'], row['author']))

            return quotes
        
        except pd.errors.EmptyDataError:
            return []
        except Exception as e:
            raise Exception(f'Error parsing CSV: {str(e)}')
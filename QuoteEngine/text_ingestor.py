"""Text file ingestor module for parsing quote files."""
from typing import List
from .ingestor_interface import IngestorInterface
from .quote_model import QuoteModel


class TextIngestor(IngestorInterface):
    """Ingestor for text files."""

    allowed_extensions = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse text file and return quotes.

        Args:
            path: Path to text file

        Returns:
            List[QuoteModel]: List of parsed quotes
        """
        if not cls.can_ingest(path):
            raise Exception('Cannot ingest this file type')

        quotes = []
        try:
            with open(path, 'r', encoding='utf-8') as f:
                for line in f:
                    line = line.strip()
                    if line:
                        parts = line.split('-')
                        if len(parts) == 2:
                            body = parts[0].strip().strip('"')
                            author = parts[1].strip().strip('"')
                            quotes.append(QuoteModel(body, author))
        except Exception as e:
            raise Exception(f'Error reading file: {str(e)}')

        return quotes

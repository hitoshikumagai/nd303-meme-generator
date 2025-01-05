from abc import ABC, abstractmethod
from typing import List
from .quote_model import QuoteModel

class IngestorInterface(ABC):
    """Abstract base class for file ingestors."""

    allowed_extensions = []

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """Check if the file can be ingested.
        Args:
            path: Path to the file
        Returns:
            bool: True if file extension is allowed
        """
        
        try:
            ext = path.split('.')[-1].lower()
            return ext in cls.allowed_extensions
        except IndexError:
            return False

    @classmethod
    @abstractmethod
    def parse(self, path: str) -> List[QuoteModel]:
        """Parse the file and create QuoteModel objects.
        Args:
            path: Path to the file
        Returns:
            List[QuoteModel]: List of parsed quotes
        """
        
        pass

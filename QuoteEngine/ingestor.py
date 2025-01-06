"""Main ingestor module that coordinates all specific ingestors."""
import os
from typing import List
from .ingestor_interface import IngestorInterface
from .quote_model import QuoteModel
from .docx_ingestor import DocxIngestor
from .pdf_ingestor import PDFIngestor
from .csv_ingestor import CSVIngestor
from .text_ingestor import TextIngestor


class Ingestor(IngestorInterface):
    """Main ingestor class that encapsulates all ingestors."""

    ingestors = [DocxIngestor, PDFIngestor, CSVIngestor, TextIngestor]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse file using appropriate ingestor.

        Args:
            path: Path to file

        Returns:
            List[QuoteModel]: List of parsed quotes
        """
        if not path or not isinstance(path, str):
            raise ValueError('Invalid path provided')

        if not os.path.exists(path):
            raise FileNotFoundError(f'File not found: {path}')

        for ingestor in cls.ingestors:
            if ingestor.can_ingest(path):
                try:
                    return ingestor.parse(path)
                except Exception as e:
                    raise Exception(
                        f'Error using {ingestor.__name__}: {str(e)}')

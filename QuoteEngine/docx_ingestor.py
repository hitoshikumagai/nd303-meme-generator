"""DOCX file ingestor module for parsing quote files."""
from typing import List
import docx
from .ingestor_interface import IngestorInterface
from .quote_model import QuoteModel

class DocxIngestor(IngestorInterface):
    """Ingestor for docx files."""

    allowed_extensions = ['docx']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse docx file and return quotes.
        
        Args:
            path: Path to docx file

        Returns:
            List[QuoteModel]: List of parsed quotes
        """
        if not cls.can_ingest(path):
            raise Exception('Cannot ingest this file type')

        quotes = []
        doc = docx.Document(path)

        for para in doc.paragraphs:
            if para.text:
                try:
                    parts = para.text.split('-')
                    if len(parts) != 2:
                        print(f'Warning: Skipping invalid format in line: {para.text}')
                        continue
                        
                    body = parts[0].strip().strip('"')
                    author = parts[1].strip()
                    
                    if not body or not author:
                        print(f'Warning: Empty quote or author in line: {para.text}')
                        continue
                        
                    quotes.append(QuoteModel(body, author))
                    
                except Exception as e:
                    print(f'Error processing paragraph: {para.text}. Error: {str(e)}')

        return quotes

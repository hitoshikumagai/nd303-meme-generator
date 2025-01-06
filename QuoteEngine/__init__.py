"""Quote Engine package for handling various quote file formats."""
from .quote_model import QuoteModel
from .ingestor_interface import IngestorInterface
from .csv_ingestor import CSVIngestor
from .docx_ingestor import DocxIngestor
from .pdf_ingestor import PDFIngestor
from .text_ingestor import TextIngestor
from .ingestor import Ingestor

__all__ = [
    'QuoteModel',
    'IngestorInterface',
    'CSVIngestor',
    'DocxIngestor',
    'PDFIngestor',
    'TextIngestor',
    'Ingestor'
]

# Version of the package
__version__ = '1.0.0'

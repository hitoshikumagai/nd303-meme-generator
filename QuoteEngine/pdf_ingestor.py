"""PDF file ingestor module for parsing quote files."""
import os
import subprocess
from typing import List
from .ingestor_interface import IngestorInterface
from .quote_model import QuoteModel

class PDFIngestor(IngestorInterface):
    """Ingestor for PDF files."""

    allowed_extensions = ['pdf']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse PDF file and return quotes.

        Args:
            path: Path to PDF file
        
        Returns:
            List[QuoteModel]: List of parsed quotes
        """
        if not cls.can_ingest(path):
            raise Exception('Cannot ingest this file type')

        try:
            # Read PDF by pdftotext and capture output
            cmd = r"""{} "{}" -""".format('xpdf', path)
            process = subprocess.Popen(
                cmd,
                shell=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            stdout, stderr = process.communicate()

            if process.returncode != 0:
                raise Exception(f'PDF conversion failed: {stderr}')

            quotes = []
            
            # Process each line from stdout
            for line in stdout.splitlines():
                line = line.strip()
                if line:
                    try:
                        parts = line.split('-')
                        if len(parts) == 2:
                            body = parts[0].strip().strip('"')
                            author = parts[1].strip()
                            quotes.append(QuoteModel(body, author))
                    except Exception as e:
                        print(f"Error processing line: {line}. Error: {e}")
            return quotes
            
        except subprocess.CalledProcessError as e:
            raise Exception(f'PDF conversion failed: {e.stderr}')

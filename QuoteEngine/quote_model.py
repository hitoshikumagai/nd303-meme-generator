"""Quote model module for representing quote data."""
class QuoteModel:
    """A class to represent a quote with body and author."""

    def __init__(self, body: str, author: str):
        """Initialize quote with body and author.

        Args:
            body: The text of the quote
            author: The author of the quote
        """
        self.body = body
        self.author = author

    def __str__(self):
        """Return string representation of the quote."""
        return f'"{self.body}" - {self.author}'

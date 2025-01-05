from PIL import Image, ImageDraw, ImageFont
import os
import random

class MemeEngine:
    """Class for creating memes by adding text to images."""

    def __init__(self, output_dir: str):
        """Initialize meme engine with output directory.

        Args:
            output_dir: Directory to save generated memes
        """
        self.output_dir = output_dir
        try:
            if not os.path.exists(self.output_dir):
                os.makedirs(self.output_dir)
        except Exception as e:
            raise OSError(f"Failed to create output directory: {str(e)}")

    def make_meme(self, img_path: str, text: str, author: str, width: int = 500) -> str:
        """Create a meme by adding text to an image.
        Args:
            img_path: Path to input image
            text: Quote text to add
            author: Quote author to add
            width: Maximum width of output image
        Returns:
            str: Path to generated meme
        """
        try:
            # Load image
            img = Image.open(img_path)

            # Calculate height to maintain aspect ratio
            aspect_ratio = img.size[0] / img.size[1]
            height = int(width / aspect_ratio)

            # Resize image
            img = img.resize((width, height))

            # Add text
            draw = ImageDraw.Draw(img)
            font = ImageFont.load_default()

            # Calculate random position for text
            x = random.randint(10, width-10)
            y = random.randint(10, height-10)

            # Add quote text and author
            text_with_author = f'"{text}" - {author}'
            draw.text((x, y), text_with_author, font=font, fill='white')

            # Save meme
            output_path = os.path.join(self.output_dir,
                                    f'meme_{random.randint(0, 1000000)}.jpg')
            img.save(output_path)
        except FileNotFoundError:
            raise FileNotFoundError(f"Could not find image file: {img_path}")
        except Exception as e:
            raise OSError(f"Error processing image: {str(e)}")
        
        return output_path

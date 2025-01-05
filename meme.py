import os
import random

# Import your Ingestor and MemeEngine classes
import argparse
from QuoteEngine import Ingestor
from QuoteEngine import QuoteModel
from MemeEngine import MemeEngine

def generate_meme(path=None, body=None, author=None):
    """ Generate a meme given an path and a quote """
    img = None
    quote = None

    if path is None:
        images = "./_data/photos/dog/"
        imgs = []
        for root, dirs, files in os.walk(images):
            imgs = [os.path.join(root, name) for name in files]

        img = random.choice(imgs)
    else:
        img = path[0]

    if body is None:
        quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                       './_data/DogQuotes/DogQuotesDOCX.docx',
                       './_data/DogQuotes/DogQuotesPDF.pdf',
                       './_data/DogQuotes/DogQuotesCSV.csv']
        quotes = []
        for f in quote_files:
            quotes.extend(Ingestor.parse(f))

        quote = random.choice(quotes)
    else:
        if author is None:
            raise Exception('Author Required if Body is Used')
        quote = QuoteModel(body, author)

    # set output directory
    output_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static')
    
    # create directory if not xists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    meme = MemeEngine(output_dir)

    path = meme.make_meme(img, quote.body, quote.author)
    return path


if __name__ == "__main__":
    # Use ArgumentParser to parse the following CLI arguments
    # path - path to an image file
    # body - quote body to add to the image
    # author - quote author to add to the image
    parser = argparse.ArgumentParser(description='Generate a meme')
    parser.add_argument('--path', type=str, help='Path to image file')
    parser.add_argument('--body', type=str, help='Quote body')
    parser.add_argument('--author', type=str, help='Quote author')

    args = parser.parse_args()
    try:
        result_path = generate_meme(args.path, args.body, args.author)
        print(f"Meme generated successfully at: {result_path}")
    except Exception as e:
        print(f"Error generating meme: {str(e)}")
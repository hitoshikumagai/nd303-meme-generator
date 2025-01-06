"""Flask application for generating memes."""
import random
import os
import requests
from flask import Flask, render_template, abort, request

# Import your Ingestor and MemeEngine classes
from QuoteEngine import Ingestor
from MemeEngine import MemeEngine

app = Flask(__name__)

meme = MemeEngine('./static')


def setup():
    """Load all resources."""
    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']

    # Use the Ingestor class to parse all files in the
    # quote_files variable
    quotes = []
    for f in quote_files:
        quotes.extend(Ingestor.parse(f))

    images_path = "./_data/photos/dog/"

    # Use the pythons standard library os class to find all
    # images within the images images_path directory
    imgs = []
    for root, dirs, files in os.walk(images_path):
        imgs.extend([os.path.join(root, name) for name in files])

    return quotes, imgs


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """Generate a random meme."""
    # Use the random python standard library class to:
    # 1. select a random image from imgs array
    # 2. select a random quote from the quotes array

    img = random.choice(imgs)
    quote = random.choice(quotes)
    path = meme.make_meme(img, quote.body, quote.author)
    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """User input for meme information."""
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """Create a user defined meme."""
    # 1. Use requests to save the image from the image_url
    #    form param to a temp local file.
    # 2. Use the meme object to generate a meme using this temp
    #    file and the body and author form paramaters.
    # 3. Remove the temporary saved image.

    # Get the form parameters
    image_url = request.form['image_url']
    body = request.form['body']
    author = request.form['author']

    try:
        # 1. Download and save image from URL
        response = requests.get(image_url)
        response.raise_for_status()  # Raises an HTTPError for bad responses

        # Create temporary file path with random number to avoid collisions
        temp_file = f'temp_{random.randint(0, 100000)}.jpg'

        # Save image to temporary file
        with open(temp_file, 'wb') as f:
            f.write(response.content)

        # 2. Generate meme using the temporary file
        path = meme.make_meme(temp_file, body, author)

    except requests.exceptions.RequestException as e:
        print(f"Error downloading image: {str(e)}")
        return render_template(
            'meme_form.html',
            error="Failed to download image. Please check the URL.")
    except Exception as e:
        print(f"Error creating meme: {str(e)}")
        return render_template(
            'meme_form.html',
            error="Failed to create meme. Please try again.")

    finally:
        # 3. Clean up - remove temporary file
        if temp_file and os.path.exists(temp_file):
            try:
                os.remove(temp_file)
            except Exception as e:
                print(f"Error removing temporary file: {str(e)}")


if __name__ == "__main__":
    app.run()

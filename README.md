# Project: Meme Generator 

## Overview
This is a multimedia application designed to dynamically generate memes by overlaying quotes on images. The project showcases several technical capabilities:

## File Processing:

* Works with multiple complex file types (PDF, Word Documents, CSV, Text files)
* Handles quote loading from various file formats
* Manages image loading, manipulation, and saving


## User Interfaces:

* Provides a command-line interface
* Includes a web service interface (using Flask)

## Usage

### Run Webapplication 
Please type `python app.py`

### Run Script
`python meme.py [--path PATH] [--body BODY] [--author AUTHOR]`
`python meme.py --path ./_data/photos/dog/xander_1.jpg --body "Hello World" --author "author"`

# Directory structure

project/
│
├── QuoteEngine/
│   ├── __init__.py
│   ├── quote_model.py
│   ├── ingestor_interface.py
│   ├── text_ingestor.py
│   ├── docx_ingestor.py
│   ├── pdf_ingestor.py
│   ├── csv_ingestor.py
│   └── ingestor.py
│
├── MemeEngine/
│   ├── __init__.py
│   └── meme_engine.py
│
├── app.py
├── meme.py
├── requirements.txt
└── README.md

# Requirements
blinker==1.9.0
certifi==2024.12.14
charset-normalizer==3.4.1
click==8.1.8
colorama==0.4.6
Flask==3.1.0
idna==3.10
itsdangerous==2.2.0
Jinja2==3.1.5
lxml==5.3.0
MarkupSafe==3.0.2
numpy==2.2.1
pandas==2.2.3
pillow==11.1.0
python-dateutil==2.9.0.post0
python-docx==1.1.2
pytz==2024.2
requests==2.32.3
six==1.17.0
typing_extensions==4.12.2
tzdata==2024.2
urllib3==2.3.0
Werkzeug==3.1.3
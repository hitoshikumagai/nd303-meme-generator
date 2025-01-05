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
`python meme.py --path "./_data/photos/dog/xander_1.jpg" --body "Hello World" --author "author"`

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
Pillow
pandas
python-docx
Flask
requests
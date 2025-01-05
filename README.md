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

### Run Web application 
Please type `python app.py`

### Run Script
`python meme.py [--path PATH] [--body BODY] [--author AUTHOR]`<br>
`python meme.py --path ./_data/photos/dog/xander_1.jpg --body "Hello World" --author "author"`<br>

# Directory structure

project/<br>
│<br>
├── QuoteEngine/<br>
│   ├── __init__.py<br>
│   ├── quote_model.py<br>
│   ├── ingestor_interface.py<br>
│   ├── text_ingestor.py<br>
│   ├── docx_ingestor.py<br>
│   ├── pdf_ingestor.py<br>
│   ├── csv_ingestor.py<br>
│   └── ingestor.py<br>
│<br>
├── MemeEngine/<br>
│   ├── __init__.py<br>
│   └── meme_engine.py<br>
│<br>
├── app.py<br>
├── meme.py<br>
├── requirements.txt<br>
└── README.md<br>

# Requirements
blinker==1.9.0<br>
certifi==2024.12.14<br>
charset-normalizer==3.4.1<br>
click==8.1.8<br>
colorama==0.4.6<br>
Flask==3.1.0<br>
idna==3.10<br>
itsdangerous==2.2.0<br>
Jinja2==3.1.5<br>
lxml==5.3.0<br>
MarkupSafe==3.0.2<br>
numpy==2.2.1<br>
pandas==2.2.3<br>
pillow==11.1.0<br>
python-dateutil==2.9.0.post0<br>
python-docx==1.1.2<br>
pytz==2024.2<br>
requests==2.32.3<br>
six==1.17.0<br>
typing_extensions==4.12.2<br>
tzdata==2024.2<br>
urllib3==2.3.0<br>
Werkzeug==3.1.3<br>